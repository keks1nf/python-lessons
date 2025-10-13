#10
nums = [6, 0, 3, 0, 5, 0, 0, 4]

pos = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[pos], nums[i] = nums[i], nums[pos]
        pos += 1

print(nums)
#9
first = {
    "first aid kit": 1,
    "lighter": 2,
    "sunglasses": 1,
    "trousers": 2,
    "hygienic set": 1,
    "flashlight": 1,
    "footwear": 2,
    "socks": 3,
    "sleeping bag": 1,
    "water jacket": 1,
    "cap": 1,
    "dishes": 2,
    "woolen gloves": 1,
    "tent": 1
}

second = {
    "first aid kit": 1,
    "lighter": 2,
    "sunglasses": 1,
    "trousers": 2,
    "hygienic set": 1,
    "flashlight": 1,
    "footwear": 2,
    "socks": 3,
    "sleeping bag": 1,
    "batteries": 4,
    "poncho": 1,
    "t-shirts": 3
}

print("In both:")
for item in first:
    if item in second:
        print(item, first[item])

print("Only in the first:")
for item in first:
    if item not in second:
        print(item, first[item])

print("Only in the other:")
for item in second:
    if item not in first:
        print(item, second[item])
#7
text = input("Введіть рядок: ")

char_counts = {}

for ch in set(text):
    count = text.count(ch)
    if count > 1:
        char_counts[ch] = count

for ch, cnt in char_counts.items():
    print(f"{ch} {cnt}")

#5
s = input("Введіть рядок: ").strip()
parts = s.split("_")
camel = "".join(word.capitalize() for word in parts if word)
print(camel)
'''
#1
Що таке список? Що можна помістити у список?
Список (list) – це впорядкована (мають індекси) змінна (можна додавати, видаляти, змінювати елементи) колекція елементів.
Може мати дублікати.
У список можна помістити: числа, рядки, булеві значення, інші списки чи словники.
#2
Чим відрізняється словник від списку?
У списку - звертаємось до елементів за індексами, а у словнику - по ключу.
#3
Який тип даних може позначатися дужками {}?
Словник (dict): d = {key1:value1, key2:value2}
Множина (set): s = {1, 2, 3}
В множині немає пар ключ-значення, тільки унікальні значення.
#4
Що означає iterable у функціях map, max тощо?
Iterable – це будь-який об’єкт, по якому можна “пройтися” в циклі for.
До iterable належать: рядки (можна пройтись по літерах), списки, кортежі, множини, словники (ітерується по ключах)
Функція map(function, iterable):
Приймає функцію та один або кілька ітерабельних об'єктів.
Застосовує вказану функцію до кожного елемента наданого ітерабельного об'єкта.
Повертає ітератор з новими значеннями, що утворилися після застосування функції.
Функція max(iterable):
Приймає ітерабельний об'єкт, як-от список або кортеж.
Знаходить і повертає найбільший елемент у цьому об'єкті.
'''
# #11
num = int(input("Введіть число (1–3999): "))


if num <= 0 or num >= 4000:
    print("Число від 1 до 3999.")
else:
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value

    print("Римське число:", result)
#12
'''
room = [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', 'R', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*']
]
'''

n = 5

room = []
for i in range(n):
    row = []
    for j in range(n):
        if i == n // 2 and j == n // 2:
            row.append('R')
        else:
            row.append('*')
    room.append(row)

x, y = n // 2, n // 2

while True:
    for row in room:
        print(' '.join(row))
    print()

    command = input("<Напрям> <Кількість клітинок> (або 0 для завершення): ")

    if command == "0":
        print("завершено")
        break


    direction, steps = command.split()
    steps = int(steps)


    room[x][y] = '*'

    if direction.upper() == 'UP':
        x = max(0, x - steps)
    elif direction.upper() == 'DOWN':
        x = min(n - 1, x + steps)
    elif direction.upper() == 'LEFT':
        y = max(0, y - steps)
    elif direction.upper() == 'RIGHT':
        y = min(n - 1, y + steps)
    else:
        print('Невідомий напрям')


    room[x][y] = 'R'


