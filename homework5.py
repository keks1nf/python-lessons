# #1
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))

for number in range(number1, number2 + 1):
    if number % 3 == 0 and number % 5 != 0:
        print(number)

number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))

number = number1
while number <= number2:
    if number % 3 == 0 and number % 5 != 0:
        print(number)
    number += 1

#2
n = int(input())

factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)

#3
name = input("Введіть своє ім'я: ")

result = name
while len(result) <= 100:
    result += name
    print(result)
#4

text = input("Введіть числа через пробіл: ")

even_count = 0
odd_count = 0

number = ""
for ch in (text + " "):   # додаємо пробіл
    if ch != " ":
        number += ch
    elif number != "":
        num = int(number)
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number = ""   # обнуляємо

print("Парних чисел: ", even_count)
print("Непарних чисел: ", odd_count)


#
# numbers = input('Введіть числа через пробіл: ') + ' '  # '2250 -3 540 11 54 3 110'
#
# odd_count = 0  # кількість парних
# even_count = 0  # кількість непарних
# sum_of_numbers = 0  # сума чисел
#
# memory = ''
#
# for char in numbers:
#     if char != ' ':
#         memory += char
#     else:  # якщо char == ' '
#         if not memory:  # if memory == ''
#             continue  # continue одразу перекидає цикл на наступну ітерацію
#
#         n = int(memory)
#
#         if n % 2 == 0:
#             odd_count += 1
#         else:
#             even_count += 1
#
#         sum_of_numbers += n
#         memory = ''
#
# print(f'Кількість парних: {odd_count}')
# print(f'Кількість непарних: {even_count}')
# print(f'Сума чисел: {sum_of_numbers}')



