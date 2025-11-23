import csv
import json
from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================================
# ІНТЕРФЕЙСИ
# ============================================================================

class Serializable(ABC):
    """Інтерфейс для серіалізації"""

    @abstractmethod
    def to_dict(self) -> dict:
        ...


class Gradable(ABC):
    """Інтерфейс для об'єктів з оцінками"""

    @abstractmethod
    def average_grade(self):
        pass


# ============================================================================
# БАЗОВІ КЛАСИ
# ============================================================================

class User(ABC):
    """Абстрактний базовий клас користувача"""

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self._notifications = []

    @abstractmethod
    def get_role(self):
        pass

    def notify(self, message: str):
        """Реалізація Notifiable"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        notification = f"[{timestamp}] {message}"
        self._notifications.append(notification)
        print(f"Message {self.name}: {message}")

    def get_notifications(self):
        return self._notifications

    def __str__(self):
        return f"{self.get_role()}: {self.name} ({self.email})"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.user_id}, name={self.name})"

    def __eq__(self, other):
        return isinstance(other, User) and self.user_id == other.user_id

    def to_dict(self):
        """Реалізація Serializable"""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'role': self.get_role()
        }


class Student(User):
    def __init__(self, user_id, name, email, student_number=""):
        super().__init__(user_id, name, email)
        self.student_number = student_number
        self.enrollments = []

    def get_role(self):
        return "Student"

    def __len__(self):
        return len(self.enrollments)

    def to_dict(self):
        data = super().to_dict()
        data['student_number'] = self.student_number
        return data


class Instructor(User):
    def __init__(self, user_id, name, email, title="", department=""):
        super().__init__(user_id, name, email)
        self.title = title
        self.department = department
        self.courses = []

    def get_role(self):
        return "Instructor"

    def assign_course(self, course):
        """Призначення курсу викладачу"""
        if course not in self.courses:
            self.courses.append(course)
            self.notify(f"Вам призначено курс: {course.title}")

    def __len__(self):
        return len(self.courses)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'title': self.title,
            'department': self.department
        })
        return data


class Admin(User):
    def get_role(self):
        return "Admin"


class Lesson:
    def __init__(self, lesson_id, title, content, duration_minutes=60):
        self.lesson_id = lesson_id
        self.title = title
        self.content = content
        self.duration_minutes = duration_minutes

    def __repr__(self):
        return f"Lesson({self.title}, {self.duration_minutes}хв)"

    def __str__(self):
        return f"{self.title} ({self.duration_minutes} хв)"

    def to_dict(self):
        return {
            'lesson_id': self.lesson_id,
            'title': self.title,
            'content': self.content,
            'duration_minutes': self.duration_minutes
        }


class Module:
    def __init__(self, module_id, title, description=""):  # description не обов'язковий
        self.module_id = module_id
        self.title = title
        self.description = description
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, lesson_id):
        self.lessons = [l for l in self.lessons if l.lesson_id != lesson_id]

    def get_total_duration(self):
        """Загальна тривалість модуля"""
        return sum(lesson.duration_minutes for lesson in self.lessons)

    def __len__(self):
        return len(self.lessons)

    def __iter__(self):
        return iter(self.lessons)

    def __str__(self):
        return f"Модуль: {self.title} ({len(self)} уроків, {self.get_total_duration()}хв)"

    def __repr__(self):
        return f"Module({self.title}, {len(self.lessons)} lessons)"

    def to_dict(self):
        return {
            'module_id': self.module_id,
            'title': self.title,
            'description': self.description,
            'lessons': [lesson.to_dict() for lesson in self.lessons]
        }


class Course:
    def __init__(self, course_id, title, description, instructor=None):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor = instructor
        self.modules = []
        self.enrollments = []

        if instructor:
            instructor.assign_course(self)

    def add_module(self, module):
        self.modules.append(module)

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)

    def get_total_duration(self):
        """Загальна тривалість курсу"""
        return sum(module.get_total_duration() for module in self.modules)

    def get_student_count(self):
        """Кількість студентів"""
        return len(self.enrollments)

    def __len__(self):
        return len(self.modules)

    def __iter__(self):
        return iter(self.modules)

    def __str__(self):
        instructor_name = self.instructor.name if self.instructor else "Не призначено"
        return f"Курс: {self.title} (викладач: {instructor_name})"

    def __repr__(self):
        return f"Course({self.title}, modules={len(self.modules)})"

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'instructor_id': self.instructor.user_id if self.instructor else None,
            'modules': [module.to_dict() for module in self.modules]
        }


class Enrollment(Gradable):
    def __init__(self, enrollment_id, student, course):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.grades = []
        self.enrollment_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.is_active = True

        student.enrollments.append(self)
        course.enrollments.append(self)
        student.notify(f"Ви зареєструвались на курс: {course.title}")

    def add_grade(self, grade):
        self.grades.append(grade)
        self.student.notify(
            f"Нова оцінка з курсу '{self.course.title}': {grade.score} балів"
        )

    def average_grade(self):
        """Реалізація Gradable"""
        if not self.grades:
            return None
        return sum(g.score for g in self.grades) / len(self.grades)

    def __str__(self):
        return f"Запис {self.student.name} на курс {self.course.title}"

    def __repr__(self):
        return f"Enrollment(student={self.student.name}, course={self.course.title})"

    def __len__(self):
        """Кількість оцінок"""
        return len(self.grades)

    def to_dict(self):
        return {
            'enrollment_id': self.enrollment_id,
            'student_id': self.student.user_id,
            'course_id': self.course.course_id,
            'enrollment_date': self.enrollment_date,
            'is_active': self.is_active,
            'grades': [grade.to_dict() for grade in self.grades]
        }


class Assignment:
    def __init__(self, assignment_id, title, description, due_date, max_score=100):
        self.assignment_id = assignment_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.max_score = max_score

    def is_overdue(self):
        """Перевірка чи прострочене завдання"""
        if isinstance(self.due_date, str):
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
        else:
            due = self.due_date
        return datetime.now() > due

    def __repr__(self):
        return f"Assignment({self.title}, due: {self.due_date})"

    def __str__(self):
        status = "Прострочено" if self.is_overdue() else "Активне"
        return f"{self.title} - {status}"

    def to_dict(self):
        return {
            'assignment_id': self.assignment_id,
            'title': self.title,
            'description': self.description,
            'due_date': str(self.due_date),
            'max_score': self.max_score
        }


class Grade:
    def __init__(self, grade_id, assignment, score, max_score=100, comment=""):
        self.grade_id = grade_id
        self.assignment = assignment
        self.score = score
        self.max_score = max_score
        self.comment = comment
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def get_percentage(self):
        """Отримати оцінку у відсотках"""
        return (self.score / self.max_score) * 100 if self.max_score > 0 else 0

    def __repr__(self):
        return f"Grade({self.assignment.title}: {self.score}/{self.max_score})"

    def __str__(self):
        return f" {self.assignment.title}: {self.score}/{self.max_score} ({self.get_percentage():.1f}%)"

    def to_dict(self):
        return {
            'grade_id': self.grade_id,
            'assignment_id': self.assignment.assignment_id,
            'score': self.score,
            'max_score': self.max_score,
            'comment': self.comment,
            'date': self.date
        }


class ScheduleEvent:
    """Подія в розкладі"""

    def __init__(self, event_id, course, title, start_time, end_time, location):
        self.event_id = event_id
        self.course = course
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def get_duration(self):
        """Тривалість події в хвилинах"""
        if isinstance(self.start_time, str):
            start = datetime.fromisoformat(self.start_time)  # YYYY-MM-DDT HH:MM:SS стандартний ISO
            end = datetime.fromisoformat(self.end_time)  # YYYY-MM-DDT HH:MM:SS
        else:
            start = self.start_time
            end = self.end_time
        return int((end - start).total_seconds() / 60)

    def __repr__(self):
        return f"ScheduleEvent({self.title} at {self.start_time})"

    def __str__(self):
        return f"{self.title} | {self.location} | {self.get_duration()}хв"

    def to_dict(self):
        return {
            'event_id': self.event_id,
            'course_id': self.course.course_id,
            'title': self.title,
            'start_time': str(self.start_time),
            'end_time': str(self.end_time),
            'location': self.location
        }


# ============================================================================
# Експорт/Імпорт
# ============================================================================

class AbstractFileExporter(ABC):
    """Абстрактна стратегія експорту"""

    @abstractmethod
    def export(self, data: list[dict], filepath: str):
        pass


class JSONExporter(AbstractFileExporter):
    """Експорт в JSON формат"""

    def export(self, data: list[dict], filepath: str):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Дані експортовано в JSON: {filepath}")


class CSVExporter(AbstractFileExporter):
    """Експорт в CSV формат"""

    def export(self, data: list[dict], filepath: str):
        if not data:
            print("Немає даних для експорту")
            return

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Дані експортовано в CSV: {filepath}")


class AbstractFileImporter(ABC):
    """Абстракт.  імпорт"""

    @abstractmethod
    def import_data(self, filepath: str) -> list[dict]:
        pass


class JSONImporter(AbstractFileImporter):
    """Імпорт з JSON"""

    def import_data(self, filepath: str) -> list[dict]:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Дані імпортовано з JSON: {filepath}")
        return data


class CSVImporter(AbstractFileImporter):
    """Імпорт з CSV"""

    def import_data(self, filepath: str) -> list[dict]:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        print(f"Дані імпортовано з CSV: {filepath}")
        return data


# ============================================================================
# Створення об'єктів
# ============================================================================

class UserFactory:
    """Фабрика для створення користувачів"""

    @staticmethod
    def create_user(role: str, user_id: str, name: str, email: str, **kwargs) -> User:
        if role.lower() == 'student':
            return Student(user_id, name, email, kwargs.get('student_number', ''))
        elif role.lower() == 'instructor':
            return Instructor(
                user_id, name, email,
                kwargs.get('title', ''),
                kwargs.get('department', '')
            )
        elif role.lower() == 'admin':
            return Admin(user_id, name, email)
        else:
            raise ValueError(f"Невідома роль: {role}")


# ============================================================================
# ГОЛОВНИЙ МЕНЕДЖЕР
# ============================================================================

class CourseManager:
    """Головний менеджер системи """

    def __init__(self):
        self.users: dict[str, User] = {}
        self.courses: dict[str, Course] = {}
        self.enrollments: dict[str, Enrollment] = {}
        self.schedule_events: list[ScheduleEvent] = []

    # ---- Користувачі ----
    def add_user(self, user: User):
        self.users[user.user_id] = user
        print(f"Користувач доданий: {user}")

    def get_user(self, user_id: str) -> User:
        return self.users.get(user_id)

    def get_students(self) -> list[Student]:
        return [u for u in self.users.values() if isinstance(u, Student)]

    def get_instructors(self) -> list[Instructor]:
        return [u for u in self.users.values() if isinstance(u, Instructor)]

    # ---- Курси ----
    def add_course(self, course: Course):
        self.courses[course.course_id] = course
        print(f"Курс доданий: {course}")

    def get_course(self, course_id: str) -> Course:
        return self.courses.get(course_id)

    # ---- Реєстрація ----
    def enroll_student(self, student: Student, course: Course) -> Enrollment:
        enrollment = Enrollment(
            f"enr_{len(self.enrollments) + 1}", student, course
        )
        self.enrollments[enrollment.enrollment_id] = enrollment
        return enrollment

    # ---- Розклад ----
    def add_schedule_event(self, event: ScheduleEvent):
        self.schedule_events.append(event)
        print(f"Подію додано: {event}")

    # ---- Експорт  ----
    def export_data(self, data_type: str, strategy: AbstractFileExporter, filepath: str):
        """Експорт даних"""
        if data_type == 'students':
            data = [s.to_dict() for s in self.get_students()]
        elif data_type == 'courses':
            data = [c.to_dict() for c in self.courses.values()]
        elif data_type == 'enrollments':
            data = [e.to_dict() for e in self.enrollments.values()]
        else:
            print(f"Невідомий тип даних: {data_type}")
            return

        strategy.export(data, filepath)

    # ---- Імпорт ----
    def import_data(self, strategy: AbstractFileImporter, filepath: str) -> list[dict]:
        """Імпорт даних"""
        return strategy.import_data(filepath)

    # ---- Збереження в JSON ----
    def save_to_json(self, filepath: str):
        """Збереження всієї системи"""
        data = {
            'users': [u.to_dict() for u in self.users.values()],
            'courses': [c.to_dict() for c in self.courses.values()],
            'enrollments': [e.to_dict() for e in self.enrollments.values()],
            'schedule': [s.to_dict() for s in self.schedule_events]
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Систему збережено: {filepath}")

    # ---- Звіти ----
    def generate_report(self, course_id: str) -> str:
        """Генерація звіту по курсу"""
        course = self.get_course(course_id)
        if not course:
            return "Курс не знайдено"

        enrollments = [e for e in self.enrollments.values() if e.course == course]
        avg_grades = [e.average_grade() for e in enrollments if e.average_grade() is not None]

        report = f"""

  ЗВІТ ПО КУРСУ: {course.title:<41}

  Викладач: {course.instructor.name if course.instructor else 'N/A':<47}
  Модулів: {len(course):<49}
  Тривалість: {course.get_total_duration()} хв{' ':<42}
  Студентів: {len(enrollments):<47}
  Середній бал: {sum(avg_grades) / len(avg_grades) if avg_grades else 0:.1f}{' ':<42}

        """
        return report


# ============================================================================
# ДЕМО
# ============================================================================

def demo():
    print("=" * 70)
    print(" СИСТЕМА КЕРУВАННЯ НАВЧАЛЬНИМИ КУРСАМИ")
    print("=" * 70)

    manager = CourseManager()

    # 1. Створення користувачів через Factory
    print("\n СТВОРЕННЯ КОРИСТУВАЧІВ")
    print("-" * 70)

    instructor = UserFactory.create_user(
        'instructor', 'I1', 'Олена Петренко', 'olena@university.ua',
        title='Професор', department='Інформатика'
    )
    manager.add_user(instructor)

    student1 = UserFactory.create_user(
        'student', 'S1', 'Марія Коваль', 'maria@student.ua',
        student_number='2024-CS-001'
    )
    manager.add_user(student1)

    student2 = UserFactory.create_user(
        'student', 'S2', 'Іван Шевченко', 'ivan@student.ua',
        student_number='2024-CS-002'
    )
    manager.add_user(student2)

    # 2. Створення курсу з модулями
    print("\n СТВОРЕННЯ КУРСУ")
    print("-" * 70)

    course = Course('CS101', 'Python для початківців', 'Вступний курс', instructor)

    module1 = Module('mod1', 'Основи Python', 'Базові концепції')
    module1.add_lesson(Lesson('l1', 'Змінні та типи даних', 'Контент...', 45))
    module1.add_lesson(Lesson('l2', 'Умови та цикли', 'if, else, while, for', 60))
    course.add_module(module1)

    module2 = Module('mod2', 'ООП в Python', 'Класи, об\'єкти, наслідування')
    module2.add_lesson(Lesson('l3', 'Класи та об\'єкти', 'Контент...', 90))
    module2.add_lesson(Lesson('l4', 'Наслідування та поліморфізм', 'Контент...', 75))
    course.add_module(module2)

    manager.add_course(course)

    # 3. Реєстрація студентів
    print("\n✍ РЕЄСТРАЦІЯ СТУДЕНТІВ")
    print("-" * 70)

    enrollment1 = manager.enroll_student(student1, course)
    enrollment2 = manager.enroll_student(student2, course)

    # 4. Завдання та оцінки
    print("\n ЗАВДАННЯ ТА ОЦІНКИ")
    print("-" * 70)

    assignment1 = Assignment('hw1', 'Домашка 1', 'Написати програму', '2025-11-20', 100)
    grade1 = Grade('g1', assignment1, 95, 100, 'Відмінно!')
    enrollment1.add_grade(grade1)

    grade2 = Grade('g2', assignment1, 87, 100, 'Добре')
    enrollment2.add_grade(grade2)

    # 5. Магічні методи
    print("\n ДЕМОНСТРАЦІЯ МАГІЧНИХ МЕТОДІВ")
    print("-" * 70)
    print(f"Курс: {course}")  # __str__
    print(f"Модулів у курсі: {len(course)}")  # __len__
    print(f"Курсів у студента: {len(student1)}")  # __len__
    print(f"Середній бал студента 1: {enrollment1.average_grade():.1f}")

    # 6. Ітерація
    print("\n СТРУКТУРА КУРСУ")
    print("-" * 70)
    for i, module in enumerate(course, 1):  # __iter__
        print(f"{i}. {module}")
        for lesson in module:  # __iter__
            print(f"   {lesson}")

    # 7. Розклад
    print("\n РОЗКЛАД")
    print("-" * 70)
    event = ScheduleEvent(
        'evt1', course, 'Лекція: ООП в Python',
        datetime(2025, 11, 20, 10, 0),
        datetime(2025, 11, 20, 11, 30),
        'Аудиторія 305'
    )
    manager.add_schedule_event(event)

    # 8. Звіт
    print("\n ЗВІТ ПО КУРСУ")
    print(manager.generate_report('CS101'))

    # 9. Експорт
    print("\n ЕКСПОРТ ДАНИХ")
    print("-" * 70)
    manager.export_data('students', JSONExporter(), 'students.json')
    manager.export_data('students', CSVExporter(), 'students.csv')
    manager.export_data('courses', JSONExporter(), 'courses.json')

    # 10. Збереження системи
    manager.save_to_json('system_backup.json')

    # 11. Сповіщення
    print("\n СПОВІЩЕННЯ СТУДЕНТА")
    print("-" * 70)
    print(f"Кількість сповіщень: {len(student1.get_notifications())}")
    for notif in student1.get_notifications():
        print(f"  {notif}")

    print("\n" + "=" * 70)
    print(" ДЕМОНСТРАЦІЯ ЗАВЕРШЕНА")
    print("=" * 70)


if __name__ == "__main__":
    demo()
