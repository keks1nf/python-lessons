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


'''
from operator import index

'''
def write_file(tasks: list) -> None:
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def read_file() -> list:
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []
'''

#Локальний шлях
#Абсолютний шлях

'''
Абсолютний шлях (повний шлях) — це повний, унікальний шлях до файлу або папки від кореневого каталогу (наприклад, `C:` або ), що включає всі папки та підпапки. 
Локальний шлях (відносний шлях) — це шлях, який вказує на розташування об'єкта відносно поточної робочої директорії, без необхідності вказувати повний шлях від кореня. 
'''


#Запис
# file = open("files\\data.txt", "w")
#
# file.write('Hello World\n')
#
# print('Hello World', file=file)
#
#
# file.close()
#Читання
file = open("files\\data.txt", "r")
print(file.read())
print(file.readline())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readline())

file.seek(0)
for line in enumerate(file, start=1):
    print(f'{index}: {line}', end='')

file.seek(0)

print(file.readlines())

file.close()

#Доповнення

file = open("files\\data.txt", "a")
print('Hi', file=file)
file.seek(0)

file.close()

