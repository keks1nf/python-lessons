
import random
import string
# Фунції

def greet():
    print('Hello World!')
'''
def ім'я_функції(параметри):
    # тіло функції
    
   def — ключове слово, яке використовується для оголошення функції;
   ім'я_функції — будь-яке ім’я, дане функції;
   параметри — значення, які приймає функція;
'''
greet()

def greet_for_name(name: str):
    print(f'Hello, {name.capitalize()}!')
greet_for_name('Bob')


# Визначення функції з двома параметрами
def add_numbers(num1: int | float , num2: int | float):
    sum_1 = num1 + num2
    print("Sum: ", sum_1)

# Виклик функції з вказанням двох аргументів
add_numbers(5, 4)


# # Визначення функції
# def find_square(num):
#     result = num * num
#     return result
#
# # Виклик функції
# square = find_square(3)
#
# print('Square:', square)

def counter (n:int):
    for _ in range(1, n + 1):
        return _  # відразу закриває функцію (як break)

result = counter(5)
print(result)


def password_generator(password_len:int):  # 8 - 30
    if password_len not in range(8, 31):
        return

    password = ''

    for _ in range(1, password_len): #Нижним подчеркиванием обычно обозначается переменная, имя которой нам не важно, так как мы ее не используем.
        password = password + random.choice(string.ascii_letters + string.digits)
    return password

print(password_generator(25))






