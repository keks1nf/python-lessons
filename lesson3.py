string_ = 'Hello world'
print(string_)
#Властивості строки

# 1.Незмінювана, повино бути дорівнює
# string = 'Hello world'
# string = string + '!'
# print(string)

# 2. Впорядкована
# 3.Індексована
# greet = 'hello'
# print(greet[1]) # "e"
# # access 1st index element
# # access 2nd index element}
# print(f'{greet[0]}') # "e"
#
# greet = input('Введіть текст')
# print (f'Довжина строки: {len(greet)'}
# print(f'Індекс {greet[len(greet) - 1]}')
#
#
# 4.Негативна індексація
# greet_1 = 'hello, world'
#
# # access 4th last element
# print(greet_1[-4]) # "e"
#
# print(f' Довжина строки: {len(greet_1)}')
# print(f' Перший елемент: {greet_1[0]}')
# print(f' Останній елемент: {greet_1[-1]}')
#
# 5.Розрізання
#
#sequence[start:stop:step]
# start – з якого індексу почати (включно)
#
# stop – до якого індексу (не включається)
#
# step – крок

# greet = 'Hello'
#
# # access character from 1st index to 3rd index
# print(greet[1:4])  # "ell"  зріз буде від 1 до 3 (праве число не включається)
# print(greet[1:])  від 1 до кінця
# print(great[:6])  від початку до 5
# print(great[:])  ввести все
#
# print(great[::2])
# print(great[::-1]) зеркальний напис

s = "Python"

print(s[0:4])    # 'Pyth' (з 0 до 3)
print(s[:4])     # 'Pyth' (початок за замовчуванням = 0)
print(s[2:])     # 'thon' (до кінця)
print(s[::2])    # 'Pto' (кожен другий символ)
print(s[::-1])   # 'nohtyP' (розворот рядка)

len('Hello world') # повертає довжину послідовності
round(5.43455, 2) # округлення числа до п-знаків
abs(-100) # абсолютне значення (модуль)
range(1,100) #створення послідовності чисел ( від 1 до 99)
type(154.5) #повертає тип обєкта (його клас)
sum((1,2,3,4,5,6,7,8)) #підрахунок суми елементів послідовності
print(ord('b'))  #повертає unicode символа



