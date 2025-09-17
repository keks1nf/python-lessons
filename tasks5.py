
#1
correct_password = "12345"   # правильний пароль

while True:
    password = input("Введіть пароль: ")
    if password == correct_password:
        print("Вхід дозволено!")
        break
    else:
        print("Неправильний пароль, спробуйте ще раз.")

# password = input('Password: ')
#
# while password != 'admin':
#     print('Неправильний пароль')
#     password = input('Password: ')
#
# print('Welcome')


# #2
'''
Як працює range()
range(stop)
: Створює послідовність від 0 до stop - 1 з кроком 1.
Приклад: range(5) генерує 0, 1, 2, 3, 4. 
range(start, stop)
: Генерує послідовність від start до stop - 1 з кроком 1.
Приклад: range(2, 5) генерує 2, 3, 4. 
range(start, stop, step)
: Генерує послідовність від start до stop - 1 з кроком step.
Приклад: range(1, 10, 2) генерує 1, 3, 5, 7, 9. 
'''
n = int(input("Введіть n: "))

for i in range(1, n + 1):
    print(str(i) * i)
# #3

n = int(input("Введіть n: "))

for i in range(n, 0, -1):   # від n до 1 reversed
    print(i, "#" * i)
    
# 3
for number in reversed(range(1, n + 1)):
    print(number, '#' * number)
