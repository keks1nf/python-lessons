import os
import re

import requests
import telebot
import urllib3
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from telebot import types

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

# =====================================================================
# 1. ПАРСЕР ГВП
# =====================================================================
URL = "https://www.zoe.com.ua/%d0%b3%d1%80%d0%b0%d1%84%d1%96%d0%ba%d0%b8-%d0%bf%d0%be%d0%b3%d0%be%d0%b4%d0%b8%d0%bd%d0%bd%d0%b8%d1%85-%d1%81%d1%82%d0%b0%d0%b1%d1%96%d0%bb%d1%96%d0%b7%d0%b0%d1%86%d1%96%d0%b9%d0%bd%d0%b8%d1%85/"


def clean_time(time_string: str) -> str:
    """Виправляє помилки у часі"""
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

    # "ПО ЗАПОРІЗЬКІЙ ОБЛАСТІ ДІЯТИМУТЬ ГПВ ..."
    # "ОНОВЛЕНО ГПВ НА ..."
    block_headers = re.finditer(
        fr"(ПО ЗАПОРІЗЬКІЙ ОБЛАСТІ ДІЯТИМУТЬ ГПВ.*?|ОНОВЛЕНО ГПВ НА [^\n]+)",
        text,
        re.IGNORECASE
    )

    header_positions = [m.start() for m in block_headers]

    header_positions.append(len(text))

    headers = re.findall(
        r"(\d{1,2}\s+\w+.*ПО ЗАПОРІЗЬКІЙ ОБЛАСТІ ДІЯТИМУТЬ ГПВ.*?|ОНОВЛЕНО ГПВ НА [^\n]+)",
        text,
        re.IGNORECASE
    )

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

        if (len(blocks) > 10):
            break

        blocks.append({
            "header": header.strip(),
            "date": date,
            "queues": queues
        })
    print(blocks)
    return blocks


load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN not found in .env!")

bot = telebot.TeleBot(BOT_TOKEN)

# ======================================================
# ГОЛОВНЕ МЕНЮ
# ======================================================
MAIN_KB = types.ReplyKeyboardMarkup(resize_keyboard=True)

btn_gpd = types.KeyboardButton("ГПВ Оновлення")
btn_weather = types.KeyboardButton("Погода Запоріжжя")
btn_news = types.KeyboardButton("Новини Запоріжжя (Suspilne)")

MAIN_KB.add(btn_gpd)
MAIN_KB.add(btn_weather)
MAIN_KB.add(btn_news)


# ======================================================
# ФУНКЦІЇ
# ======================================================

def format_all_blocks(blocks):
    """Форматує всі блоки ГПВ."""
    if not blocks:
        return "⚠️ Нічого не знайдено на сайті."

    parts = []
    for b in blocks:

        if len(parts) > 3:
            break
        header = b.get("header") or ""
        date = b.get("date") or ""
        queues = b.get("queues") or {}

        if date:
            parts.append(f"📅 *{date}*")
        else:
            parts.append("📅 *дата не вказана*")

        parts.append(f"📰 _{header}_\n")

        def sort_key(k):
            try:
                major, minor = k.split(".")
                return int(major), int(minor)
            except:
                return 999, 999

        for q in sorted(queues.keys(), key=sort_key):
            parts.append(f"*{q}*: `{queues[q]}`")

        parts.append("\n" + "—" * 30 + "\n")
    print(parts)
    return "\n".join(parts)


# Функція погоди
def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=47.85&longitude=35.17&current_weather=true&timezone=Europe/Kyiv"
    r = requests.get(url).json()

    w = r["current_weather"]
    temp = w["temperature"]
    wind = w["windspeed"]
    code = w["weathercode"]

    conditions = {
        0: "☀️ Ясно",
        1: "🌤 Трохи хмарно",
        2: "⛅ Хмарно",
        3: "☁️ Похмуро",
        45: "🌫 Туман",
        48: "🌫 Осадковий туман",
        51: "🌦 Легкий дощ",
        61: "🌧 Дощ",
        71: "❄️ Сніг",
    }

    cond = conditions.get(code, "🌈 Невідома погода")

    return (
        f"<b>Погода в Запоріжжі</b>\n"
        f"{cond}\n"
        f"🌡 Температура: <b>{temp}°C</b>\n"
        f"💨 Вітер: <b>{wind} км/год</b>"
    )


# Новини Запоріжжя
def get_suspilne_zp_news(limit=5):
    url = "https://suspilne.media/zaporizhzhia/latest/"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print("Помилка HTTP:", e)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")

    # НОВИНИ — тільки карточки з класом c-article-card
    items = soup.select(".c-article-card")

    news = []
    for it in items[:limit]:
        print(it.select_one("a").get('href'))
        print(it.select_one(".c-article-card__headline-inner").text)
        print(it.select_one("time").text)
        # print(it.select_one("#foo").text)
        # print(it.select_one('[data-type="latest"]').text)
        # main_content > section > div.l-category.js-articles > article:nth-child(2) > div > a.c-article-card__headline > span

        href = it.select_one("a").get('href')
        if not href:
            continue

        # Заголовок
        title_tag = it.select_one(".c-article-card__headline-inner")
        title = title_tag.get_text(strip=True) if title_tag else "Без назви"

        # Дата
        date_tag = it.select_one("time")
        date = date_tag.get_text(strip=True) if date_tag else "дата невідома"

        # Повне посилання
        link = href if href.startswith("http") else "https://suspilne.media" + href

        news.append({
            "title": title,
            "date": date,
            "link": link
        })

    return news


# ======================================================
# КОМАНДИ
# ======================================================

@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    bot.send_message(
        message.chat.id,
        "Привіт 👋\n\nОбери потрібну опцію нижче:",
        reply_markup=MAIN_KB
    )


# ======================================================
# КНОПКИ
# ======================================================

@bot.message_handler(func=lambda m: m.text == "Погода Запоріжжя")
def handle_weather(message):
    try:
        bot.send_message(message.chat.id, get_weather(), parse_mode="HTML")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Помилка погоди: {e}")


@bot.message_handler(func=lambda m: m.text == "Новини Запоріжжя (Suspilne)")
def handle_suspilne_news(message):
    news = get_suspilne_zp_news(limit=5)

    if not news:
        bot.send_message(message.chat.id, "⚠️ Не вдалося отримати новини")
        return

    text_parts = []
    for n in news:
        text_parts.append(
            f"📰 <b>{n['title']}</b>\n"
            f"📅 {n['date']}\n"
            f"🔗 {n['link']}"
        )

    bot.send_message(message.chat.id, "\n\n".join(text_parts), parse_mode="HTML")


@bot.message_handler(func=lambda m: m.text == "ГПВ Оновлення")
def cmd_gpd(message):
    bot.send_message(message.chat.id, format_all_blocks(blocks=parse_page()), parse_mode="Markdown")


# ======================================================
#  ЗАПУСК БОТА
# ======================================================
print("Bot is running...")
bot.infinity_polling()
