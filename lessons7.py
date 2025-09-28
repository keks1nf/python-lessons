# Методи строк
#Метод - це фукція що описана та викликається всередині об*єкту
# Клас це str, об*єкт - 'Hello, world'

string = 'Hello, world'

# 1. Case методи
print(string.upper()) # призводить строку до верхнього регістру
print(string.lower()) # призводить строку до нижнього регістру

print('hElLO, WoRlD'.capitalize()) # перша літера велика інші маленькі
print('hElLO, WoRlD'.title()) # кожне слово з великої
print(string.swapcase()) # змінює регістр на протилежний

#2. bool - методи  (повертають True/False)
print(string.isupper()) # True якщо всі літери великі
print(string.islower()) # True якщо всі літери маленькі
print(string.isdigit()) # True якщо всі елементи цифри
print(string.isalpha()) # True якщо всі елементи букви
print(string.startswith('Hel'))  # True якщо строка починається з вказаної послідовності
print(string.endswith('rld')) # True якщо строка закінчується вказаною послідовністю

#3. Робота з підстроками
print(string.index('l')) #  повертає індекс першої підстроки
print(string.index('world')) #працює і з підстроками
#print(string.index('1')) # якщо її немає Value Error

print(string.find('l')) #аналогічно index()
print(string.find('world'))
print(string.find('1')) # на відміну від index() якщо її немає -1

print(string.replace('l', '*')) #змінює всі __old на __new
print(string.replace('world', '_'))
print(string.replace('o', '{{{WORLD}}}'))

print("   a    b   c d   g   h f  ".strip()) # відрізає пробіли з країв
print("|||1||2||3||4||5||".strip('|')) # можна міняти символ, який треба прибрати

print(string.count('l'))  #кількість елементів

# 4. split та join
numbers = '-1 100    542   7764   10   5444 12   '
split_result = numbers.split()
print(','.join(split_result))
print(','.join(str(number) for number in range(1, 101) if number % 2 == 0 )) # генератор

#Генератор паролю
import string
import random

# password = ""
# for _ in range(15): # повторити 15 разів
#     password += random.choice(string.ascii_letters + string.digits)
#
# print(password)


password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
print(f'Ваш пароль: {password}')

random.random()
print (int(random.random()*100))