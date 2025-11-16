from abc import ABC, abstractmethod
from datetime import datetime


class User(ABC):
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.get_role()}: {self.name} ({self.email})"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.user_id}, name={self.name})"

    def __eq__(self, other):
        return isinstance(other, User) and self.user_id == other.user_id


class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.enrollments = []

    def get_role(self):
        return "Student"

    def __len__(self):
        return len(self.enrollments)


class Instructor(User):
    def __init__(self, user_id, name, email, title=""):
        super().__init__(user_id, name, email)
        self.title = title

    def get_role(self):
        return "Instructor"


class Admin(User):
    def get_role(self):
        return "Admin"


class Lesson:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"Lesson({self.title})"


class Module:
    def __init__(self, title):
        self.title = title
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def __len__(self):
        return len(self.lessons)

    def __iter__(self):
        return iter(self.lessons)

    def __str__(self):
        return f"Модуль: {self.title} ({len(self)} уроків)"


class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.modules = []
        self.enrollments = []

    def add_module(self, module):
        self.modules.append(module)

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)

    def __len__(self):
        return len(self.modules)

    def __iter__(self):
        return iter(self.modules)

    def __str__(self):
        return f"Курс: {self.title} (викладач: {self.instructor.name})"

    def __repr__(self):
        return f"Course({self.title}, modules={len(self.modules)})"


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grades = []
        student.enrollments.append(self)
        course.enrollments.append(self)

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return None
        return sum(g.score for g in self.grades) / len(self.grades)

    def __str__(self):
        return f"Запис {self.student.name} на курс {self.course.title}"

    def __repr__(self):
        return f"Enrollment(student={self.student.name}, course={self.course.title})"


class Assignment:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return f"Assignment({self.title})"


class Grade:
    def __init__(self, assignment, score, comment=""):
        self.assignment = assignment
        self.score = score
        self.comment = comment
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __repr__(self):
        return f"Grade({self.assignment.title}: {self.score})"

# def demo():
#     instructor = Instructor("I1", "Олена", "olena@example.com")
#     student = Student("S1", "Марія", "maria@example.com")
#
#     course = Course("Python для початківців", instructor)
#     module1 = Module("Основи Python")
#     module1.add_lesson(Lesson("Змінні", "Оголошення змінних"))
#     module1.add_lesson(Lesson("Умови", "if, else, elif"))
#     course.add_module(module1)
#
#     enrollment = Enrollment(student, course)
#
#     assignment = Assignment("Домашка 1", "Написати програму", "2025-11-20")
#     enrollment.add_grade(Grade(assignment, 95, "Супер!"))
#
#     print(course)
#     print(f"Модулів у курсі: {len(course)}")
#     print("Список модулів:")
#     for m in course:
#         print("  ", m)
#     print(f"Оцінка: {enrollment.grades[0]}")
#     print(f"Середній бал: {enrollment.average_grade()}")
#
#
# if __name__ == "__main__":
#     demo()
