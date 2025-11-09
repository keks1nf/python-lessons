
from abc import ABC, abstractmethod

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def say_hi(self):
        return f'Hello {self.name}, my age is {self.age}'

class Human:  # батьківський
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return f'Привіт, я людина {self.name}, мені {self.age} років!'


class Student(Human):  # дочірній
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grades = []

    def say_hi(self):
        return f'Я студент! Мої оцінка: {self.grades}'

    def add_grade(self, grade):
        self.grades.append(grade)


def interface(human: Human):
    print(f'Привітання: {human.say_hi()}')


alice = Human('Аліса', 20)
bob = Student('Боб', 35)

interface(alice)
interface(bob)


class Animal(ABC):
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    @abstractmethod
    def sound(self):
        raise NotImplementedError

class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Dog")


    def sound(self):
        return 'Aff'

dog = Dog("Paul")


