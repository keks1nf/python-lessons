# Обробник винятків
'''
Виняток	Причина помилки
AssertionError	Виникає, коли assertоператор не виконується.
AttributeError	Виникає, коли не вдається присвоїти атрибут або виконати посилання.
EOFError	Викликається, коли input()функція досягає умови кінця файлу.
FloatingPointError	Викликається, коли операція з плаваючою комою не вдається.
GeneratorExit	close()Підвищує, коли викликається метод генератора .
ImportError	Виникає, коли імпортований модуль не знайдено.
IndexError	Виникає, коли індекс послідовності виходить за межі діапазону.
KeyError	Виникає, коли ключ не знайдено у словнику.
KeyboardInterrupt	Виникає, коли користувач натискає клавішу переривання ( Ctrl+C або Delete).
MemoryError	Виникає, коли операція не вистачає пам'яті.
NameError	Виникає, коли змінна не знайдена в локальній або глобальній області видимості.
NotImplementedError	Отримано абстрактними методами.
OSError	Виникає, коли системна робота викликає системну помилку.
OverflowError	Виникає, коли результат арифметичної операції занадто великий для представлення.
ReferenceError	Виникає, коли для доступу до референта, зібраного зі сміття, використовується слабкий проксі-сервер посилання.
RuntimeError	Виникає, коли помилка не підпадає під жодну іншу категорію.
StopIteration	Викликається next()функцією, щоб вказати, що ітератор більше не повертає жодного елемента.
SyntaxError	Викликається синтаксичним аналізатором у разі виявлення синтаксичної помилки.
IndentationError	Виникає, коли є неправильний відступ.
TabError	Виникає, коли відступ складається з невідповідних табуляцій та пробілів.
SystemError	Виникає, коли інтерпретатор виявляє внутрішню помилку.
SystemExit	Підвищено sys.exit()функцією.
TypeError	Виникає, коли функція або операція застосовується до об'єкта неправильного типу.
UnboundLocalError	Виникає, коли у функції або методі робиться посилання на локальну змінну, але до цієї змінної не прив'язано жодне значення.
UnicodeError	Виникає, коли виникає помилка кодування або декодування, пов'язана з Unicode.
UnicodeEncodeError	Виникає, коли під час кодування виникає помилка, пов'язана з Unicode.
UnicodeDecodeError	Виникає, коли під час декодування виникає помилка, пов'язана з Unicode.
UnicodeTranslateError	Виникає, коли під час перекладу виникає помилка, пов'язана з Unicode.
ValueError	Виникає, коли функція отримує аргумент правильного типу, але неправильне значення.
ZeroDivisionError	Виникає, коли другий операнд операції ділення або поділу за модулем дорівнює нулю.

'''
from unittest import case


class MyException(Exception):
    def __str__(self):
        return 'MyException'

def raiser(n: int) -> None:
    match n:
        case 1:
            raise ValueError
        case 2:
            raise ZeroDivisionError
        case 3:
            raise IndexError('IndexError!!')
        case 4:
            raise MyException
        case 5:
            raise KeyboardInterrupt


try:
    raiser(5)

    number_1 = int(input('Число 1: '))
    number_2 = int(input('Число 2: '))

    result = number_1/number_2
    print(f'Результат: {result}')
except ValueError:
    print('Ви ввели не число!')
except ZeroDivisionError:
    print('Ділення на нуль!')
except ArithmeticError:
    print('Інша математична помилка!')
except MyException:
    print('Спрацював мій виняток!!')
except Exception as e:
    print(e)
else:
    print('Else')
finally:
    print('finally')





