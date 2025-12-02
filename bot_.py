import re

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://www.zoe.com.ua/%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/"


# ======================== CLEANER ====================================

def clean_time_range(text: str) -> str:
    """Очищення помилок форматування часу."""
    text = text.replace(";", ":")
    text = re.sub(r'\s*[-—–]\s*', ' – ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    def fix_time(t):
        if re.match(r'^\d:\d{2}$', t):
            t = "0" + t
        if re.match(r'^\d{2}:\d$', t):
            t = t[:-1] + "0" + t[-1]
        if re.match(r'^\d$', t):
            t = f"0{t}:00"
        if re.match(r'^\d{2}$', t):
            t = f"{t}:00"
        return t

    def repl(m):
        return fix_time(m.group(0))

    text = re.sub(r'\d{1,2}:\d{1,2}|\d{1,2}', repl, text)
    text = text.replace("24:00", "00:00")

    return text


# ======================== PARSER ====================================

def fetch_latest_gpv():
    resp = requests.get(URL, verify=False)
    soup = BeautifulSoup(resp.text, "html.parser")

    posts = soup.select("article")

    if not posts:
        return {"error": "Не знайдено новин"}

    # шукаємо першу новину, яка містить ОПУБЛІКОВАНИЙ ГПВ
    gpv_post = None
    for post in posts:
        if "ГПВ" in post.text or "Графік" in post.text or "оновлено" in post.text.lower():
            gpv_post = post
            break

    if gpv_post is None:
        return {"error": "Не знайдено новини з ГПВ"}

    link = gpv_post.select_one("a").get("href")
    return parse_gpv_page(link)


def parse_gpv_page(url):
    resp = requests.get(url, verify=False)
    soup = BeautifulSoup(resp.text, "html.parser")

    # беремо тільки контент поста
    article = soup.select_one("article")
    if not article:
        return {"error": "Стаття не знайдена"}

    text = article.get_text("\n", strip=True)

    # шукаємо дату тільки в перших 300 символах — де зазвичай пишуть “ГПВ оновлено…”
    header_part = text[:300]

    # шукаємо дати
    date_pattern = r"[0-3]?\d\.[01]\d\.\d{4}"
    dates = re.findall(date_pattern, header_part)

    # якщо знайдено дивну дату типу 2023 — ігноруємо
    dates = [d for d in dates if not d.endswith("2023")]

    # fallback: якщо дат нема → None
    if not dates:
        dates = ["не знайдено"]

    # ================= РОЗКЛАД ПО ЧЕРГАХ ======================
    queue_pattern = r"(\d\.\d)\s*:\s*([^\n]+)"
    raw_blocks = re.findall(queue_pattern, text)

    queues = {sub: clean_time_range(times) for sub, times in raw_blocks}

    return {
        "url": url,
        "dates": dates,
        "queues": queues,
    }


# ======================== RUN ====================================

result = fetch_latest_gpv()
print(result)
