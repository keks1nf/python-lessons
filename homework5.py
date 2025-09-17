# #1
# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))
#
# for number in range(number1, number2 + 1):
#     if number % 3 == 0 and number % 5 != 0:
#         print(number)

# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))
#
# number = number1
# while number <= number2:
#     if number % 3 == 0 and number % 5 != 0:
#         print(number)
#     number += 1

#2
# n = int(input())
#
# factorial = 1
#
# for i in range(2, n+1):
#     factorial *= i
#
# print(factorial)

#3
# name = input("Введіть своє ім'я: ")
#
# result = name
# while len(result) <= 100:
#     result += name
#     print(result)
#4

# index = 0
# numbers = input("Enter numbers separated by space: ")
# number = ''
#
# even_count = 0
# odd_count = 0
#
# while index < len(numbers):
#     if numbers[index] != ' ':
#         number += numbers[index]
#     else:
#         if number != '':
#             num = int(number)
#             if num % 2 == 0:
#                 even_count += 1
#             else:
#                 odd_count += 1
#         number = ''
#     index += 1
#
# #останнє число
# if number != '':
#     num = int(number)
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print(f"Even numbers: {even_count}")
# print(f"Odd numbers: {odd_count}")

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





