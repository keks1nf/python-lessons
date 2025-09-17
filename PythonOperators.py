# Арифметичні оператори в Python

a = 7
b = 2

# addition
print ('Sum: ', a + b)  # сума

# subtraction
print ('Subtraction: ', a - b)   # Віднімання

# multiplication
print ('Multiplication: ', a * b)  # Множення

# division
print ('Division: ', a / b) # Ділення

# floor division
print ('Floor Division: ', a // b) # цільночисельне ділення

# modulo
print ('Modulo: ', a % b)  # оператор ділення з остачею

# a to the power b
print ('Power: ', a ** b)   # розрахунок степенів (піднесення до степеня)


# Оператори присвоєння в Python

# assign 10 to a
a_1 = 10

# assign 5 to b
b = 5

# assign the sum of a and b to a
a_1 += b      # a_1 = a_1 + b

print(a_1)

# Output: 15

a = 7
# +=	Додавання
a += 1 # a = a + 1
# -=	віднімання
a -= 3 # a = a - 3
# *=	множення
a *= 4 # a = a * 4
# /=	ділення
a /= 3 # a = a / 3
# %=	Призначення залишків
a %= 10 # a = a % 10
# **=	Присвоєння степеня
a **= 10 # a = a ** 10


# Оператори порівняння в Python
a = 5

b = 2

# equal to operator
print('a == b =', a == b)   #Дорівнює

# not equal to operator
print('a != b =', a != b) #Не дорівнює

# greater than operator
print('a > b =', a > b)  #Більше ніж

# less than operator
print('a < b =', a < b)  #Менше ніж

# greater than or equal to operator
print('a >= b =', a >= b)   #Більше або дорівнює

# less than or equal to operator
print('a <= b =', a <= b)  #Менше або дорівнює


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



# Оператор тотожності

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True
print(x3 is y3)  # prints False

# is	True якщо операнди ідентичні (посилаються на один і той самий об'єкт)	x is True
# is not	True якщо операнди не ідентичні (не посилаються на один і той самий об'єкт)	x is not True



# Оператори членства

message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

# in	True якщо значення/змінна знайдено в послідовності	5 in x
# not in	True якщо значення/змінна не знайдено в послідовності	5 not in x
