
class Student:
    def __init__(self, name: str, *grades: int):
        self.name = name
        self.grades = list(grades)

    def __repr__(self):
        return f'Студент {self.name}. Середній бал: {self.average_grade()}'

    def __add__(self, other):  # при додаванні розраховуємо загальний середній бал
        sum_of_grades = self.grades + other.grades  # об'єднуємо оцінки
        return round(sum(sum_of_grades) / len(sum_of_grades), 2)

    def __gt__(self, other):  # self > other
        return self.average_grade() > other.average_grade()

    def __getitem__(self, item):
        item -= 1

        if item >= len(self.grades):
            raise IndexError

        return self.grades[item]

    def add_grade(self, grade: int):
        if type(grade) != int:
            raise ValueError('Оцінка має бути числом!')

        self.grades.append(grade)

    def average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)


class StudentGroup:
    def __init__(self, name: str):
        self.name = name
        self.students: list[Student] = []

    def __iter__(self):
        return iter(self.students)

    def add_students(self, *students: Student):
        for st in students:
            if type(st) != Student:
                raise ValueError('До групи можна додавати тільки студента!')

            if st in self.students:
                print(f'{st.name} вже є у групі!')
                continue

            self.students.append(st)

    def get_best_student(self):
        # return max(self.students, key=lambda student: student.average_grade())  # student1 > student2 ...
        return max(self.students)
    



bob = Student('Боб', 10, 11, 9, 8, 7, 10, 8)
alice = Student('Аліса', 11, 12, 11, 10)
john = Student('Джон', 6, 8, 10, 5, 6, 8)

group = StudentGroup('DA51')

group.add_students(bob)
group.add_students(bob, alice)  # боб не повинен додатись вдруге
group.add_students(john, alice)  # аліса теж не повинна додатись

print(group.get_best_student())

print(bob + alice)

'''
Етапи ітерації в Python:

1. Python створює ітератор об'єкту: iter()
2. Python витягує наступний елемент ітератору: next()
3. Як тільки ітератор закінчується (закінчуються елементи), він генерує виняток(помилку) StopIteration

'''

print('Ітерація групи:')
for el in group:
    print(el)

print(group[1])