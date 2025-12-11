import re

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://www.zoe.com.ua/%d0%b3%d1%80%d0%b0%d1%84%d1%96%d0%ba%d0%b8-%d0%bf%d0%be%d0%b3%d0%be%d0%b4%d0%b8%d0%bd%d0%bd%d0%b8%d1%85-%d1%81%d1%82%d0%b0%d0%b1%d1%96%d0%bb%d1%96%d0%b7%d0%b0%d1%86%d1%96%d0%b9%d0%bd%d0%b8%d1%85/"


def clean_time(time_string: str) -> str:
    """Виправляє помилки у часі типу '07;30', '7:3', '24:00'."""
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
    block_headers = re.finditer(
        fr"(ПО ЗАПОРІЗЬКІЙ ОБЛАСТІ ДІЯТИМУТЬ ГПВ.*?|ОНОВЛЕНО ГПВ НА [^\n]+)",
        text,
        re.IGNORECASE
    )

    header_positions = [m.start() for m in block_headers]

    # Додати кінець тексту для останнього блоку
    header_positions.append(len(text))

    headers = re.findall(
        r"(\d{1,2}\s+\w+.*ПО ЗАПОРІЗЬКІЙ ОБЛАСТІ ДІЯТИМУТЬ ГПВ.*?|ОНОВЛЕНО ГПВ НА [^\n]+)",
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

        if (len(blocks) > 10):
            break

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

# bot.py
import os
import json
import time
from dotenv import load_dotenv
import telebot
from telebot import types

# Імпортуємо парсер — вважатимемо, що parser.parse_page() повертає list блоків
# блок = { "header": "...", "date": "dd.mm.yyyy" or None, "queues": { "1.1": "05:30 – 08:00, ..." } }
# from parser import parse_page

# Завантажуємо токен
load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN not found in env. Create a .env file with BOT_TOKEN=...")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)  # будемо форматувати самі (plain/Markdown)

# Спроба отримати клавіатуру з модуля markups (якщо існує)
try:
    import markups
except Exception:
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(types.KeyboardButton("/gpd"), types.KeyboardButton("/start"))


def format_all_blocks(blocks):
    """Форматує всі блоки в один текст для відправки."""
    if not blocks:
        return "⚠️ Нічого не знайдено на сайті."

    parts = []
    for b in blocks:
        header = b.get("header") or ""
        date = b.get("date") or ""
        queues = b.get("queues") or {}

        # Заголовок і дата
        if date:
            parts.append(f"📅 *{date}*")
        else:
            parts.append("📅 *дата не вказана*")

        parts.append(f"📰 _{header}_\n")

        # Сортуємо черги по натуральному порядку (1.1, 1.2, 2.1...)
        def sort_key(k):
            try:
                major, minor = k.split(".")
                return (int(major), int(minor))
            except Exception:
                return (999, 999)

        for q in sorted(queues.keys(), key=sort_key):
            times = queues[q]
            parts.append(f"*{q}*: `{times}`")

        parts.append("\n" + ("—" * 30) + "\n")

    # Збираємо в один текст. Використаємо Markdown-like formatting,
    # Telebot може відправити як MarkdownV2, але краще відправляти plain щоб уникнути ескейпів.
    # Оскільки рядки містять backticks, відправимо як plain text.
    return "\n".join(parts)


@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    txt = (
        "Привіт! 👋\n\n"
        "Я бот, який витягує ГПВ з сайту ZOE.\n\n"
        "Команди:\n"
        "/gpd — отримати всі поточні блоки ГПВ одним повідомленням\n"
        "/raw — отримати сирі блоки у JSON (для налагодження)\n"
    )
    bot.send_message(message.chat.id, txt)


@bot.message_handler(commands=["gpd"])
def cmd_gpd(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "⏳ Парсинг сайту… (працюю)")
    try:
        blocks = parse_page()
    except Exception as e:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg.message_id,
            text=f"❌ Помилка при парсингу: {e}\nСпробуйте пізніше."
        )
        return

    # Формуємо одне повідомлення
    text = format_all_blocks(blocks)

    # Якщо текст занадто довгий, розбиваємо на частини (Telegram має обмеження ~4096)
    MAX = 4000
    if len(text) <= MAX:
        bot.edit_message_text(chat_id=chat_id, message_id=msg.message_id, text=text)
    else:
        bot.delete_message(chat_id, msg.message_id)
        # Розбиваємо по логічним розділам (за блоком)
        # Відправляємо перший шматок відразу
        pieces = []
        current = ""
        for b in blocks:
            blk_text = format_all_blocks([b])
            if len(current) + len(blk_text) + 2 > MAX:
                pieces.append(current)
                current = blk_text
            else:
                current = current + "\n" + blk_text
        if current:
            pieces.append(current)

        for p in pieces:
            # невеликий тайм-аут між повідомленнями, щоб не потрапити під rate limit
            bot.send_message(chat_id, p)
            time.sleep(0.25)


@bot.message_handler(commands=["raw"])
def cmd_raw(message):
    chat_id = message.chat.id
    try:
        blocks = parse_page()
    except Exception as e:
        bot.send_message(chat_id, f"❌ Помилка парсингу: {e}")
        return

    # Відправляємо JSON (якщо занадто довго — віддамо файл)
    payload = json.dumps(blocks, ensure_ascii=False, indent=2)
    if len(payload) < 3000:
        bot.send_message(chat_id, f"<pre>{payload}</pre>", parse_mode="HTML")
    else:
        # збережемо у тимчасовий файл і відправимо
        fname = "gpv_raw.json"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(payload)
        with open(fname, "rb") as f:
            bot.send_document(chat_id, f)
        os.remove(fname)


@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id, "Я не зрозумів. Спробуй команду /gpd або /start")


if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
