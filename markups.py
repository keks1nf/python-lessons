from telebot import types


def get_start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # контейнер для клавіатурних кнопок

    btn1 = types.KeyboardButton(text='Рандомайзер🙌')
    btn2 = types.KeyboardButton(text='Цікаві сайти👌')
    btn3 = types.KeyboardButton(text='Вгадай число🤩')
    btn4 = types.KeyboardButton(text='Оцінка боту🥳')

    markup.add(btn1, btn2, btn3)
    markup.add(btn4)

    return markup


def get_url_markups():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text='Офіційний сайт Python', url='https://www.python.org/'))
    markup.add(types.InlineKeyboardButton(text='Практикум Python', url='https://pythonexercises.rozh2sch.org.ua/'))

    return markup


def get_grades_markup(username: str):
    markup = types.InlineKeyboardMarkup()

    # можна циклом
    markup.add(types.InlineKeyboardButton(text='5🤩',
                                          callback_data=f'grade_5_{username}'))  # username можна дістати і з callback
    markup.add(types.InlineKeyboardButton(text='4😁', callback_data=f'grade_4_{username}'))
    markup.add(types.InlineKeyboardButton(text='3😢', callback_data=f'grade_3_{username}'))
    markup.add(types.InlineKeyboardButton(text='2😣', callback_data=f'grade_2_{username}'))
    markup.add(types.InlineKeyboardButton(text='1🤬', callback_data=f'grade_1_{username}'))

    return markup


def get_admin_answer_markup(user_id: int):
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text='Відповісти👀', callback_data=f'adminanswer_{user_id}'))

    return markup
