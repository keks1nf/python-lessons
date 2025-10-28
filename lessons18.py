
# 1 Клас -> ∞ Об'єкт

class Human:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):  # викликається, коли об'єкт класу перетворюється на строку
        return f'Human: {self.name}'

    def __int__(self):  # викликається, коли об'єкт класу перетворюється на число
        return self.age  # наші об'єкти будуть повертати вік в якості числа

    def __len__(self):  # спрацьовує, коли self потрапляє в len (len(self))
        return int(self.height)

    def say_hello(self):
        return f'Hello, my name is {self.name}! I`m {self.age} y.o.'

    def birthday(self, years: int):
        self.age += years
        print(f'{self.name} виповнилося {self.age} років!!!')


bob = Human('Bob', 28, 192.40)  # створення об'єкту, або ініціалізація класу
alice = Human('Alice', 18, 150.35)

# alice.name = 'Alice'  # Так НЕ ТРЕБА робити!!!
# alice.age = 18
# alice.height = 152.53

bob.birthday(20)
alice.birthday(2)

print(bob.say_hello())   # -> Human.say_hello(bob)
print(alice.say_hello())

print(bob)
print(alice)

print(int(bob) + 1)
print(len(alice))
