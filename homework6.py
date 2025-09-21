#1
count = int(input('Скільки чисел треба ввести? '))

memory = ''
for numbers in range(1, count + 1):
    num = input(f'Введіть число {numbers}: ')

    memory = f'{memory} {numbers}'

print(f'Результат:', {memory})
#2
text = 'cvfgbvklhilkfddfgfbgdsafdvtyutio'

count = 0

for char in text:
    if char in 'AaEeIiOoUu':
        count += 1

if count > 0:
    print("Кількість голосних:", count)
else:
    print("У тексті немає голосних букв!")
#3
import string

text = input('Введіть текст: ')
letter_len = int(input("Введіть кількість букв: "))

count = 0

memory = ""
for ch in (text + " "):
    if ch not in " " and ch not in string.punctuation + "«»":
        memory += ch
    else:
        if len(memory) == letter_len:
            count += 1
        memory = ""


print(f'{count} слова довжиною {letter_len} літери ')







