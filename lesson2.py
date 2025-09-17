# Типи даних

string = '100'  # str послідовність символів текст
name = 'Python'
print(name)

message = 'Python for beginners'
print(message)

integer = 100 # int  ціле число
print(integer)

num1 = 5
print(num1, 'is of type', type(num1))

num1 = "a"
print(num1 *10)  # aaaaaaa


float_ = 100.5 # float  дробове число
print(float)

print(round(10.43454534, 3))

boolean = True  # bool - логічний тип даних
print(boolean)

none = None # порожні дані
print(none)

'''
 Вводить в консоль 2 числа
 Результатом виведіть суму цих чисел



num1 = int(input('Enter a number: ')) # input завжди повертає строку !!!
num2 = int(input('Enter another number: '))

sum_of_nums = num1 + num2
print(sum_of_nums)
print ('Сума чисел:', + str(sum_of_nums))
print(f'сума чисел: {sum_of_nums}')
'''
# | Звідки ➡️ Куди     | Приклад                                       | Результат                              |
# | ------------------ | --------------------------------------------- | -------------------------------------- |
# | `int → float`      | `float(5)`                                    | `5.0`                                  |
# | `float → int`      | `int(3.9)`                                    | `3` (обрізає дробову частину)          |
# | `int → str`        | `str(42)`                                     | `'42'`                                 |
# | `str → int`        | `int("42")`                                   | `42`                                   |
# | `str → float`      | `float("3.14")`                               | `3.14`                                 |
# | `float → str`      | `str(2.5)`                                    | `'2.5'`                                |
# | `int/float → bool` | `bool(0)` → `False`<br>`bool(7)` → `True`     |                                        |
# | `str → bool`       | `bool("")` → `False`<br>`bool("hi")` → `True` |                                        |
# | `list → tuple`     | `tuple([1,2,3])`                              | `(1, 2, 3)`                            |
# | `tuple → list`     | `list((1,2,3))`                               | `[1, 2, 3]`                            |
# | `set → list`       | `list({1,2,3})`                               | `[1, 2, 3]` (порядок може змінюватись) |
# | `list → set`       | `set([1,2,2,3])`                              | `{1, 2, 3}` (дублікати зникають)       |

# Перетворення
# int
print(int('10')+ 1)
# print(int('avbkjbkadjbvk'))  # ValueError
# print(int('50.5'))  # Аналогічно ValueError
#print(int('100.55')) буде помилка
print(int(5.99)) # 5  не округлення, візьме цілу частку

print(int('10_00_00')) # можна вводити для зручності
print(int(True)) # 1
print(int(False)) # 0
# на str (просто накладає лапки)
print(str(True) + '!')
print(str(False) + '!')

# на float
print(float(1))
print(float('1'))
print(float('1.1'))

print(0.1+0.2) # 0.30000000000000004
print(0.3-0.1) # 0.19999999999999998
print(round(0.1 + 0.2, 2))  # 0.3
print(round(0.3 - 0.1, 2))  # 0.2









