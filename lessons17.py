# import sqlite3
#
#
# with sqlite3.connect("files\\database.sl3") as connection:  # створення самого підключення
#     cursor = connection.cursor()  # створення курсору
#
#
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS humans (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             age INTEGER);
#     ''')  # створення таблиці, якщо не існує
#
#     cursor.execute('INSERT INTO humans (name, age) VALUES ("Оксана", 20);')  # додавання нового запису до БД
#     cursor.execute('INSERT INTO humans (name, age) VALUES ("Микола", 20);')
#     cursor.execute('INSERT INTO humans (name, age) VALUES ("Олександр", 20);')
#
#     cursor.execute('SELECT * FROM humans')
#
#     result = cursor.fetchall()
#
# for id, name, age in result:
#     print(f'{id}. {name}: {age} років')

import sqlite3

def add_human(name: str, age: int) -> None:
    with sqlite3.connect("files\\database.sl3") as connection:
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS humans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            );
        ''')


        cursor.execute("INSERT INTO humans (name, age) VALUES (?, ?);", (name, age))


        connection.commit()

        print(f"Додано: {name}, {age} років")



# add_human("Павло", 35)
# add_human("Христина", 45)
# add_human("Володимир", 23)



def print_all():
    with sqlite3.connect("files/database.sl3") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM humans;")
        result = cursor.fetchall()

        if not result:
            print("У таблиці 'humans' немає записів.")
            return

        print("\n--- Усі записи з таблиці 'humans' ---")
        for person in result:
            id, name, age = person
            print(f"{id}. {name}: {age} років")



print_all()
