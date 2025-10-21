'''
Функція	Дія
json.dump(obj, file)	записує Python-об’єкт у JSON-файл
json.load(file)	читає JSON-файл і повертає Python-об’єкт
json.dumps(obj)	перетворює Python-об’єкт у JSON-рядок
json.loads(str)	перетворює JSON-рядок у Python-об’єкт

Основні режими роботи з файлами
Режим	Повна назва	Що робить
'r'	read	🔹 Відкриває файл для читання. Файл має вже існувати.
'w'	write	🔹 Відкриває файл для запису. Якщо файл існує — усе в ньому стирається! Якщо не існує — створюється новий файл.
'a'	append	🔹 Відкриває файл для додавання (новий текст додається в кінець, нічого не стирається).
'x'	exclusive creation	🔹 Створює новий файл, якщо такого ще немає. Якщо файл існує — буде помилка.

Типи даних у JSON
JSON підтримує лише кілька базових типів:

String (рядок):

"Hello World"

Number (число):

43
Boolean (логічне значення):

true

Null (порожнє значення):

null

Array (масив):

[1, 2, "three", false]
Object (об’єкт):

{
  "name": "Alex",
  "age": 28,
  "isAdmin": true
}

'''
import json

# python_data = {
#     'name': 10 ,
#     'surname': 'Hello world',
#     'grades': [10,15,20,25],
#     'year': False,
#     'month': None
# }
#
# with open('files\\data.json', 'w') as file:
#     json.dump(python_data, file, indent=4)
#
# with open('files\\data.json', 'r') as file:
#     python_data = json.load(file)
#
# print(python_data)

data = {
    'name': 'Alex',
    'age': 28,
    'isAdmin': True,
    'grades': [10,15,20,25]
}
json_data = json.dumps(data, indent=4)
print(json_data)

python_data = json.loads(json_data)
print(python_data)