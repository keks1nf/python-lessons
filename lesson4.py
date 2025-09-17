# Порівняння

#1. порівняння чисел (числа порівнюються математично)

n = 10  # символ присвоєння '='

print(n > 2) # True
print(n < 2) # False

print(n == 2)  # порівняння на рівність
print(n == 10.0) #True
print(n != 10) #False
print(n >= 10) #True
print(n <= 25) #True


#2 порівняння строк (строки порівнюються на ідентичність)
s="abcd"
print(s > "ABCD")  # на < та > строки порівнюються за Unicode

print(s == "abcd ") #False зайвий пробіл
print(s == "aBcd") #False одна літера велика
print(10 == "10.0") #False

print(n != "aabcd") # True

print('a' in s)  #True повертає якщо лівий об єкт знаходиться у правому
print('abc' in s) #True
print('abd' in s) #False бо підстроки "abd" немає у s

"""

"""
# number = int(input('Enter a number: '))
# #Введіть число: 10
# #10 – це додатне число.
# #Оператор поза оператором if.
#
# # check if number is greater than 0
# if number > 0:  # якщо
#     print(f'{number} is a positive number.')
# elif number < 0:
#     print(f'{number} is a negative number.') # в ішому випадку,  якщо
# else:  # інакше, в усіх інших випадках
#     print('Zero')
#
# print('A statement outside the if statement.')

'''
Структура умови 
- 1 if починає умову
- стільки завгодно elif (в тому числі і 0)
- 1 або 0 else 
'''

number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
        print('Number is 0')

    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')


# Обєднання порівнянь

print(5 > 1 and 10 < 20)

# Логічні оператори Python
a = 5
b = 6

print((a > 2) and (b >= 6))    # True

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False
# and	а та б	Логічне І :  True лише якщо обидва операнди True
# or	а або б	Логічне АБО :  True якщо хоча б один з операндів True
# not	не  	Логічне НЕ :  Tru якщо операнд є False, і навпаки.

