import string
import random

def func (a, b, *args, key1=100, key2=200, **kwargs):
    print(f'Позиційні аргументи: {a}, {b}')
    print(f'Нескінчені позиції: {args}') # * буде використаний усередині функції з параметром, довільна кількість позиційних аргументів буде згрупована у кортеж.
    print(f'Ключові аргументи: {key1}, {key2}')
    print(f'Нескінчені ключові: {kwargs}') # **, щоб згрупувати іменовані аргументи у словник, де імена аргументів стануть ключами, а їх значення - відповідними значеннями у словнику

func(10, 20, 1,2,3,4,5, key1=0, x=12, y=13)

#print(10, 20,30,40,50, sep=',', end='!')

def mult_numbers(*numbers: int | float):
    total = 1
    for n in numbers:
        total *= n
    return total
print(mult_numbers(10,20,30,40,50))

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(mult_numbers(*nums))

print(*'hello')


def password_generator(password_len: int, include_punktuation = False):

    password = ""
    pattern = string.ascii_letters + string.digits

    if include_punktuation:
        pattern += string.punctuation
    for _ in range(password_len):
        password += random.choice(pattern)

    return password

print(password_generator(25))
print(password_generator(25, include_punktuation=True))


d = {
    'key1': 1,
     }
d.update({'key2': 2, 'key3': 3})
print(d)