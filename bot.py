import json
import os
import random
import time
from functools import partial

import telebot  # для Telegram
from dotenv import load_dotenv  # для змінних середи
from telebot import types

import markups  # наш модуль для контейнерів з кнопками

guess_game = {}  # прогрес гри
leaderboard = []  # таблиця лідерів

LEADERBOARD_FILE = "leaderboard.json"

if os.path.exists(LEADERBOARD_FILE):
    with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
        leaderboard = json.load(f)


def save_leaderboard():
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, ensure_ascii=False, indent=4)


load_dotenv()

TOKEN = os.getenv('TOKEN')
admin_id = int(os.getenv('ADMIN_ID'))

bot = telebot.TeleBot(TOKEN)


def send_admin_answer(message: types.Message, user_id: int):
    bot.send_message(message.chat.id, text='Дякую, надсилаю відповідь!')
    bot.send_message(user_id, text=f'Адміністратор дав відповідь на вашу оцінку:\n{message.text}')


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    chat_id = message.chat.id
    username = message.from_user.username if message.from_user.username else message.from_user.first_name

    markup = markups.get_start_markup()

    bot.send_message(chat_id,
                     text=f'Привіт, {username}! Я тестовий бот!😁',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message: types.Message):
    chat_id = message.chat.id

    message_text = message.text
    username = message.from_user.username if message.from_user.username else message.from_user.first_name

    if chat_id in guess_game:
        if message_text == 'Скасувати':
            del guess_game[chat_id]
            bot.send_message(chat_id, "Гру скасовано", reply_markup=markups.get_start_markup())
            return

        if not message_text.isdigit():
            bot.send_message(chat_id, "Введи число, а не текст")
            return

        number = int(message_text)
        game = guess_game[chat_id]
        game["attempts"] += 1

        if number < game["number"]:
            bot.send_message(chat_id, "Більше")
            return

        if number > game["number"]:
            bot.send_message(chat_id, "Менше")
            return

        duration = round(time.time() - game["start"], 2)

        username = message.from_user.username or message.from_user.first_name

        # додати у лідерборд
        leaderboard.append({
            "user": username,
            "attempts": game["attempts"],
            "time": duration
        })

        leaderboard.sort(key=lambda x: (x["attempts"], x["time"]))
        save_leaderboard()

        del guess_game[chat_id]

        bot.send_message(
            chat_id,
            text=f"🎉 ТИ ВГАДАВ!\n"
                 f"Спроби: {game['attempts']}\n"
                 f"Час: {duration} с",
            reply_markup=markups.get_start_markup()
        )
        return

    # === МЕНЮ ===
    match message_text:
        case 'Рандомайзер🙌':
            pass
        case 'Цікаві сайти👌':
            markup = markups.get_url_markups()

            bot.send_message(chat_id,
                             text='Ось цікаві сайти по Python:',
                             reply_markup=markup)
        case 'Вгадай число🤩':
            guess_game[chat_id] = {
                "number": random.randint(1, 100),
                "attempts": 0,
                "start": time.time()
            }

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('Скасувати'))

            bot.send_message(chat_id,
                             text="Я загадав число від 1 до 100! Введи свій варіант 😊",
                             reply_markup=markup)

        case 'Оцінка боту🥳':
            markup = markups.get_grades_markup(username)

            bot.send_message(chat_id,
                             text='Постав оцінку :)',
                             reply_markup=markup)
        case _:
            bot.send_message(chat_id, text=f'Я бачу твоє повідомлення\n"{message_text}"\nАле поки відповідати не вмію😒')


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('grade'))
def get_grade(callback: types.CallbackQuery):
    split_data = callback.data.split('_', maxsplit=2)

    grade = int(split_data[1])
    username = split_data[2]

    bot.answer_callback_query(callback.id, text=f'Дякую за оцінку, {username}', show_alert=False)
    bot.edit_message_text(
        text='Оцінку поставлено!❤️',
        chat_id=callback.message.chat.id,
        message_id=callback.message.id,
        reply_markup=types.InlineKeyboardMarkup()
    )

    markup = markups.get_admin_answer_markup(callback.message.chat.id)
    bot.send_message(admin_id, text=f'{username} поставив оцінку: {grade}', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('adminanswer'))
def prepare_admin_answer(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    user_id = int(callback.data.split('_')[1])

    if chat_id != admin_id:
        return

    bot.edit_message_text(
        text='Відповідаємо',
        chat_id=chat_id,
        message_id=callback.message.id,
        reply_markup=types.InlineKeyboardMarkup())

    message = bot.send_message(chat_id, text='Напиши свою відповідь у наступному повідомленні:')
    bot.register_next_step_handler(message, partial(send_admin_answer, user_id=user_id))


bot.polling(none_stop=True)
