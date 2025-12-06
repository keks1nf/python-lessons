import re

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://www.zoe.com.ua/%d0%b3%d1%80%d0%b0%d1%84%d1%96%d0%ba%d0%b8-%d0%bf%d0%be%d0%b3%d0%be%d0%b4%d0%b8%d0%bd%d0%bd%d0%b8%d1%85-%d1%81%d1%82%d0%b0%d0%b1%d1%96%d0%bb%d1%96%d0%b7%d0%b0%d1%86%d1%96%d0%b9%d0%bd%d0%b8%d1%85/"


def clean_time(time_string: str) -> str:
    """Виправляє помилки у часі."""
    s = time_string.replace(";", ":")
    s = re.sub(r'\s*[-—–]\s*', " – ", s)

    def normalize_time(t):
        # Якщо t = 7:3 → 07:03
        parts = t.split(":")
        if len(parts) == 2:
            h, m = parts
            h = h.zfill(2)
            m = m.zfill(2)
            return f"{h}:{m}"
        # Якщо t = 7 → 07:00
        if t.isdigit():
            return t.zfill(2) + ":00"
        return t

    s = re.sub(
        r'\d{1,2}:\d{1,2}|\d{1,2}',
        lambda m: normalize_time(m.group(0)),
        s
    )

    s = s.replace("24:00", "00:00")
    return s


def parse_page():
    resp = requests.get(URL, verify=False)
    soup = BeautifulSoup(resp.text, "html.parser")

    article = soup.select_one("article")
    text = article.get_text("\n", strip=True)

    blocks = []

    # === ЗНАЙТИ ВСІ БЛОКИ ГПВ ===
    # Заголовки-блоки:
    # "ПО ЗАПОРІЗЬКІЙ ОБЛАСТІ ДІЯТИМУТЬ ГПВ ..."
    # "ОНОВЛЕНО ГПВ НА ..."
    block_headers = re.compile(
        r"(?s)(?:"
        r"(\d{1,2}\.\d{1,2}\.\d{4}|\d{1,2}\s+[а-яіїєґА-ЯІЇЄҐ]+(?:\s+\d{4})?)\s+ПО\s+ЗАПОРІЗЬКІЙ\s+ОБЛАСТІ\s+ДІЯТИМУТЬ\s+ГПВ(.*?)(?=\n\n|\r\n\r\n|$)"
        r"|"
        r"ОНОВЛЕНО\s+ГПВ\s+НА\s+([^\n]+)"
        r")",
        re.IGNORECASE
    )

    matches = list(block_headers.finditer(text))
    header_positions = [m.start() for m in matches]

    # Додати кінець тексту для останнього блоку
    header_positions.append(len(text))

    headers = re.findall(
        r"(ПО ЗАПОРІЗЬКІЙ ОБЛАСТІ ДІЯТИМУТЬ ГПВ.*?|ОНОВЛЕНО ГПВ НА [^\n]+)",
        text,
        re.IGNORECASE
    )

    # === ВИТЯГТИ КОЖЕН БЛОК ===
    for i in range(len(headers)):
        header = headers[i]
        start = header_positions[i]
        end = header_positions[i + 1]

        block_text = text[start:end]

        # Витягнути дату
        date_match = re.search(r"\d{1,2}\.\d{1,2}\.\d{4}", block_text)
        date = date_match.group(0) if date_match else None

        # Витягнути черги
        queues = dict(re.findall(r"(\d\.\d)\s*:\s*([^\n]+)", block_text))

        # Очистити часи
        for k in queues:
            queues[k] = clean_time(queues[k])

        blocks.append({
            "header": header.strip(),
            "date": date,
            "queues": queues
        })

    return blocks


# === RUN ===
parsed = parse_page()
for block in parsed:
    print(block)
    print("=" * 50)
