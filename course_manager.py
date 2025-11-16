"""
CourseManager - Платформа керування навчальними курсами
Демонстрація ООП, SOLID, патернів проектування в Python
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional, Protocol
from enum import Enum
import json
import csv
from pathlib import Path


# ============================================================================
# ІНТЕРФЕЙСИ ТА АБСТРАКЦІЇ (Interface Segregation Principle)
# ============================================================================

class Serializable(Protocol):
    """Інтерфейс для серіалізації об'єктів"""
    def to_dict(self) -> dict:
        ...
    
    @classmethod
    def from_dict(cls, data: dict):
        ...


class Notifiable(ABC):
    """Абстрактний інтерфейс для сповіщень"""
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class Gradable(ABC):
    """Інтерфейс для об'єктів, які можна оцінювати"""
    @abstractmethod
    def calculate_grade(self) -> float:
        pass


# ============================================================================
# БАЗОВІ МОДЕЛІ (Single Responsibility Principle)
# ============================================================================

class User(ABC):
    """
    Абстрактний базовий клас для всіх користувачів
    Демонструє наслідування та Liskov Substitution Principle
    """
    def __init__(self, user_id: str, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._notifications: List[str] = []
    
    @property
    def user_id(self) -> str:
        return self._user_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def email(self) -> str:
        return self._email
    
    @abstractmethod
    def get_role(self) -> str:
        """Кожен підклас визначає свою роль"""
        pass
    
    def notify(self, message: str) -> None:
        """Реалізація Notifiable"""
        self._notifications.append(f"[{datetime.now()}] {message}")
        print(f"📧 {self.name}: {message}")
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.user_id}, name={self.name})"
    
    def __str__(self) -> str:
        return f"{self.name} ({self.get_role()})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id
    
    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'role': self.get_role()
        }


class Student(User):
    """Студент - підклас User (LSP)"""
    def __init__(self, user_id: str, name: str, email: str, student_number: str):
        super().__init__(user_id, name, email)
        self.student_number = student_number
        self.enrollments: List['Enrollment'] = []
    
    def get_role(self) -> str:
        return "Student"
    
    def enroll(self, enrollment: 'Enrollment') -> None:
        self.enrollments.append(enrollment)
        self.notify(f"Ви зареєструвались на курс: {enrollment.course.title}")
    
    def get_average_grade(self) -> float:
        """Обчислення середнього балу студента"""
        grades = [e.get_final_grade() for e in self.enrollments if e.get_final_grade() is not None]
        return sum(grades) / len(grades) if grades else 0.0
    
    def __len__(self) -> int:
        """Кількість курсів студента"""
        return len(self.enrollments)
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data['student_number'] = self.student_number
        return data


class Instructor(User):
    """Викладач - підклас User (LSP)"""
    def __init__(self, user_id: str, name: str, email: str, department: str):
        super().__init__(user_id, name, email)
        self.department = department
        self.courses: List['Course'] = []
    
    def get_role(self) -> str:
        return "Instructor"
    
    def assign_course(self, course: 'Course') -> None:
        self.courses.append(course)
        self.notify(f"Вам призначено курс: {course.title}")
    
    def __len__(self) -> int:
        """Кількість курсів викладача"""
        return len(self.courses)
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data['department'] = self.department
        return data


class Admin(User):
    """Адміністратор системи"""
    def __init__(self, user_id: str, name: str, email: str):
        super().__init__(user_id, name, email)
        self.permissions = ['manage_users', 'manage_courses', 'view_reports']
    
    def get_role(self) -> str:
        return "Admin"


# ============================================================================
# НАВЧАЛЬНІ МАТЕРІАЛИ (Composition)
# ============================================================================

@dataclass
class Lesson:
    """Окремий урок"""
    lesson_id: str
    title: str
    content: str
    duration_minutes: int
    order: int = 0
    
    def __repr__(self) -> str:
        return f"Lesson({self.title}, {self.duration_minutes}хв)"
    
    def to_dict(self) -> dict:
        return {
            'lesson_id': self.lesson_id,
            'title': self.title,
            'content': self.content,
            'duration_minutes': self.duration_minutes,
            'order': self.order
        }


class Module:
    """
    Модуль курсу - містить уроки (Composition)
    Single Responsibility: відповідає тільки за структуру модуля
    """
    def __init__(self, module_id: str, title: str, description: str):
        self.module_id = module_id
        self.title = title
        self.description = description
        self._lessons: List[Lesson] = []
    
    def add_lesson(self, lesson: Lesson) -> None:
        lesson.order = len(self._lessons)
        self._lessons.append(lesson)
    
    def remove_lesson(self, lesson_id: str) -> bool:
        for lesson in self._lessons:
            if lesson.lesson_id == lesson_id:
                self._lessons.remove(lesson)
                return True
        return False
    
    def get_total_duration(self) -> int:
        """Загальна тривалість модуля"""
        return sum(lesson.duration_minutes for lesson in self._lessons)
    
    def __len__(self) -> int:
        return len(self._lessons)
    
    def __iter__(self):
        return iter(self._lessons)
    
    def __repr__(self) -> str:
        return f"Module({self.title}, {len(self._lessons)} lessons)"
    
    def to_dict(self) -> dict:
        return {
            'module_id': self.module_id,
            'title': self.title,
            'description': self.description,
            'lessons': [lesson.to_dict() for lesson in self._lessons]
        }


class Course:
    """
    Курс - містить модулі (Composition)
    Демонструє композицію та агрегацію
    """
    def __init__(self, course_id: str, title: str, description: str, 
                 instructor: Optional[Instructor] = None):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor = instructor  # Агрегація
        self._modules: List[Module] = []  # Композиція
        self.max_students = 30
        
        if instructor:
            instructor.assign_course(self)
    
    def add_module(self, module: Module) -> None:
        self._modules.append(module)
    
    def remove_module(self, module_id: str) -> bool:
        for module in self._modules:
            if module.module_id == module_id:
                self._modules.remove(module)
                return True
        return False
    
    def get_total_duration(self) -> int:
        """Загальна тривалість курсу"""
        return sum(module.get_total_duration() for module in self._modules)
    
    def __len__(self) -> int:
        """Кількість модулів"""
        return len(self._modules)
    
    def __iter__(self):
        return iter(self._modules)
    
    def __repr__(self) -> str:
        return f"Course({self.title}, {len(self._modules)} modules)"
    
    def __str__(self) -> str:
        instructor_name = self.instructor.name if self.instructor else "TBA"
        return f"📚 {self.title} (Викладач: {instructor_name})"
    
    def to_dict(self) -> dict:
        return {
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'instructor_id': self.instructor.user_id if self.instructor else None,
            'modules': [module.to_dict() for module in self._modules],
            'max_students': self.max_students
        }


# ============================================================================
# ОЦІНЮВАННЯ (Gradable implementation)
# ============================================================================

class GradeType(Enum):
    ASSIGNMENT = "assignment"
    EXAM = "exam"
    QUIZ = "quiz"
    PROJECT = "project"


@dataclass
class Grade:
    """Оцінка за завдання"""
    grade_id: str
    student: Student
    assignment_name: str
    score: float
    max_score: float
    grade_type: GradeType
    date: datetime = field(default_factory=datetime.now)
    
    def get_percentage(self) -> float:
        return (self.score / self.max_score) * 100 if self.max_score > 0 else 0
    
    def __repr__(self) -> str:
        return f"Grade({self.assignment_name}: {self.score}/{self.max_score})"
    
    def to_dict(self) -> dict:
        return {
            'grade_id': self.grade_id,
            'student_id': self.student.user_id,
            'assignment_name': self.assignment_name,
            'score': self.score,
            'max_score': self.max_score,
            'grade_type': self.grade_type.value,
            'date': self.date.isoformat()
        }


class Assignment:
    """Завдання для студентів"""
    def __init__(self, assignment_id: str, title: str, description: str, 
                 max_score: float, deadline: datetime):
        self.assignment_id = assignment_id
        self.title = title
        self.description = description
        self.max_score = max_score
        self.deadline = deadline
        self.submissions: Dict[str, float] = {}
    
    def submit(self, student_id: str, score: float) -> None:
        self.submissions[student_id] = score
    
    def __repr__(self) -> str:
        return f"Assignment({self.title}, deadline: {self.deadline.date()})"


class Enrollment(Gradable):
    """
    Реєстрація студента на курс (зв'язокMany-to-Many)
    Implements Gradable
    """
    def __init__(self, enrollment_id: str, student: Student, course: Course):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()
        self.grades: List[Grade] = []
        self.is_active = True
    
    def add_grade(self, grade: Grade) -> None:
        self.grades.append(grade)
        self.student.notify(f"Нова оцінка з курсу {self.course.title}: {grade.score}/{grade.max_score}")
    
    def calculate_grade(self) -> float:
        """Реалізація Gradable - обчислення фінальної оцінки"""
        if not self.grades:
            return 0.0
        total_percentage = sum(g.get_percentage() for g in self.grades)
        return total_percentage / len(self.grades)
    
    def get_final_grade(self) -> Optional[float]:
        """Отримання фінальної оцінки"""
        return self.calculate_grade() if self.grades else None
    
    def __repr__(self) -> str:
        return f"Enrollment({self.student.name} → {self.course.title})"
    
    def to_dict(self) -> dict:
        return {
            'enrollment_id': self.enrollment_id,
            'student_id': self.student.user_id,
            'course_id': self.course.course_id,
            'enrollment_date': self.enrollment_date.isoformat(),
            'is_active': self.is_active,
            'grades': [grade.to_dict() for grade in self.grades]
        }


# ============================================================================
# РОЗКЛАД
# ============================================================================

@dataclass
class ScheduleEvent:
    """Подія в розкладі"""
    event_id: str
    course: Course
    title: str
    start_time: datetime
    end_time: datetime
    location: str
    
    def get_duration(self) -> int:
        """Тривалість події в хвилинах"""
        return int((self.end_time - self.start_time).total_seconds() / 60)
    
    def __repr__(self) -> str:
        return f"Event({self.title} at {self.start_time})"
    
    def to_dict(self) -> dict:
        return {
            'event_id': self.event_id,
            'course_id': self.course.course_id,
            'title': self.title,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'location': self.location
        }


# ============================================================================
# ПАТЕРН STRATEGY - Стратегії експорту/імпорту (OCP)
# ============================================================================

class ExportStrategy(ABC):
    """Абстрактна стратегія експорту (Open/Closed Principle)"""
    @abstractmethod
    def export(self, data: List[dict], filepath: Path) -> None:
        pass


class JSONExportStrategy(ExportStrategy):
    """Експорт у JSON"""
    def export(self, data: List[dict], filepath: Path) -> None:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Дані експортовано в JSON: {filepath}")


class CSVExportStrategy(ExportStrategy):
    """Експорт у CSV"""
    def export(self, data: List[dict], filepath: Path) -> None:
        if not data:
            return
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Дані експортовано в CSV: {filepath}")


# ============================================================================
# ПАТЕРН FACTORY - Фабрика користувачів (DIP)
# ============================================================================

class UserFactory:
    """Фабрика для створення користувачів (Dependency Inversion)"""
    
    @staticmethod
    def create_user(role: str, user_id: str, name: str, email: str, **kwargs) -> User:
        if role.lower() == 'student':
            return Student(user_id, name, email, kwargs.get('student_number', 'N/A'))
        elif role.lower() == 'instructor':
            return Instructor(user_id, name, email, kwargs.get('department', 'General'))
        elif role.lower() == 'admin':
            return Admin(user_id, name, email)
        else:
            raise ValueError(f"Невідома роль: {role}")


# ============================================================================
# ПАТЕРН OBSERVER - Спостерігач для сповіщень
# ============================================================================

class CourseObserver(ABC):
    """Абстрактний спостерігач"""
    @abstractmethod
    def update(self, event: str, data: dict) -> None:
        pass


class EmailNotifier(CourseObserver):
    """Сповіщення через email"""
    def update(self, event: str, data: dict) -> None:
        print(f"📧 Email сповіщення: {event} - {data}")


class CourseSubject:
    """Суб'єкт спостереження"""
    def __init__(self):
        self._observers: List[CourseObserver] = []
    
    def attach(self, observer: CourseObserver) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: CourseObserver) -> None:
        self._observers.remove(observer)
    
    def notify(self, event: str, data: dict) -> None:
        for observer in self._observers:
            observer.update(event, data)


# ============================================================================
# ГОЛОВНИЙ МЕНЕДЖЕР СИСТЕМИ (Facade Pattern)
# ============================================================================

class CourseManager:
    """
    Головний клас для керування всією системою
    Демонструє Facade Pattern та інтеграцію всіх компонентів
    """
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.courses: Dict[str, Course] = {}
        self.enrollments: Dict[str, Enrollment] = {}
        self.schedule_events: List[ScheduleEvent] = []
        self.subject = CourseSubject()
        
        # Додаємо спостерігачів
        self.subject.attach(EmailNotifier())
    
    # ---- Керування користувачами ----
    def add_user(self, user: User) -> None:
        self.users[user.user_id] = user
        print(f"✅ Користувач доданий: {user}")
    
    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)
    
    def get_students(self) -> List[Student]:
        return [u for u in self.users.values() if isinstance(u, Student)]
    
    def get_instructors(self) -> List[Instructor]:
        return [u for u in self.users.values() if isinstance(u, Instructor)]
    
    # ---- Керування курсами ----
    def add_course(self, course: Course) -> None:
        self.courses[course.course_id] = course
        self.subject.notify('course_added', {'course_id': course.course_id, 'title': course.title})
        print(f"✅ Курс доданий: {course}")
    
    def get_course(self, course_id: str) -> Optional[Course]:
        return self.courses.get(course_id)
    
    # ---- Реєстрація на курси ----
    def enroll_student(self, student: Student, course: Course) -> Enrollment:
        enrollment = Enrollment(
            f"enr_{len(self.enrollments) + 1}",
            student,
            course
        )
        self.enrollments[enrollment.enrollment_id] = enrollment
        student.enroll(enrollment)
        
        self.subject.notify('student_enrolled', {
            'student': student.name,
            'course': course.title
        })
        return enrollment
    
    # ---- Додавання оцінок ----
    def add_grade(self, enrollment: Enrollment, assignment_name: str, 
                  score: float, max_score: float, grade_type: GradeType) -> Grade:
        grade = Grade(
            f"grade_{len(enrollment.grades) + 1}",
            enrollment.student,
            assignment_name,
            score,
            max_score,
            grade_type
        )
        enrollment.add_grade(grade)
        return grade
    
    # ---- Розклад ----
    def add_schedule_event(self, event: ScheduleEvent) -> None:
        self.schedule_events.append(event)
        print(f"✅ Подію додано до розкладу: {event}")
    
    # ---- Експорт даних (Strategy Pattern) ----
    def export_courses(self, strategy: ExportStrategy, filepath: Path) -> None:
        """Експорт курсів з використанням вибраної стратегії (OCP)"""
        data = [course.to_dict() for course in self.courses.values()]
        strategy.export(data, filepath)
    
    def export_students(self, strategy: ExportStrategy, filepath: Path) -> None:
        """Експорт студентів"""
        data = [student.to_dict() for student in self.get_students()]
        strategy.export(data, filepath)
    
    # ---- Збереження системи ----
    def save_to_json(self, filepath: Path) -> None:
        """Збереження всієї системи в JSON"""
        data = {
            'users': [user.to_dict() for user in self.users.values()],
            'courses': [course.to_dict() for course in self.courses.values()],
            'enrollments': [enr.to_dict() for enr in self.enrollments.values()]
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"💾 Систему збережено: {filepath}")
    
    # ---- Звіти ----
    def generate_course_report(self, course_id: str) -> str:
        """Генерація звіту по курсу"""
        course = self.get_course(course_id)
        if not course:
            return "Курс не знайдено"
        
        enrollments = [e for e in self.enrollments.values() if e.course == course]
        avg_grades = [e.calculate_grade() for e in enrollments if e.grades]
        
        report = f"""
╔══════════════════════════════════════════════════════════╗
║           ЗВІТ ПО КУРСУ: {course.title:<30}║
╠══════════════════════════════════════════════════════════╣
║ Викладач: {course.instructor.name if course.instructor else 'N/A':<46}║
║ Модулів: {len(course):<48}║
║ Тривалість: {course.get_total_duration()} хв{' ':<40}║
║ Студентів: {len(enrollments):<46}║
║ Середній бал: {sum(avg_grades)/len(avg_grades) if avg_grades else 0:.2f}%{' ':<39}║
╚══════════════════════════════════════════════════════════╝
        """
        return report
    
    def __repr__(self) -> str:
        return f"CourseManager(users={len(self.users)}, courses={len(self.courses)})"


# ============================================================================
# ДЕМОНСТРАЦІЯ РОБОТИ СИСТЕМИ
# ============================================================================

def main():
    """Демонстрація можливостей системи"""
    
    print("=" * 70)
    print("🎓 СИСТЕМА КЕРУВАННЯ НАВЧАЛЬНИМИ КУРСАМИ")
    print("=" * 70)
    
    # Створюємо менеджер
    manager = CourseManager()
    
    # 1. Створюємо користувачів через Factory (DIP)
    print("\n📋 СТВОРЕННЯ КОРИСТУВАЧІВ")
    print("-" * 70)
    
    instructor1 = UserFactory.create_user(
        'instructor', 'inst001', 'Олена Петренко', 'olena@university.ua',
        department='Інформатика'
    )
    manager.add_user(instructor1)
    
    student1 = UserFactory.create_user(
        'student', 'std001', 'Іван Коваль', 'ivan@student.ua',
        student_number='2024-CS-001'
    )
    manager.add_user(student1)
    
    student2 = UserFactory.create_user(
        'student', 'std002', 'Марія Шевченко', 'maria@student.ua',
        student_number='2024-CS-002'
    )
    manager.add_user(student2)
    
    # 2. Створюємо курс з модулями (Composition)
    print("\n📚 СТВОРЕННЯ КУРСУ")
    print("-" * 70)
    
    course = Course(
        'CS101',
        'Основи Python програмування',
        'Вступний курс до Python',
        instructor1
    )
    
    # Додаємо модулі та уроки
    module1 = Module('mod1', 'Введення в Python', 'Базові концепції')
    module1.add_lesson(Lesson('l1', 'Змінні та типи даних', 'Контент...', 45))
    module1.add_lesson(Lesson('l2', 'Умови та цикли', 'Контент...', 60))
    course.add_module(module1)
    
    module2 = Module('mod2', 'ООП в Python', 'Об\'єктно-орієнтоване програмування')
    module2.add_lesson(Lesson('l3', 'Класи та об\'єкти', 'Контент...', 90))
    module2.add_lesson(Lesson('l4', 'Наслідування', 'Контент...', 75))
    course.add_module(module2)
    
    manager.add_course(course)
    
    # 3. Реєстрація студентів
    print("\n✍️ РЕЄСТРАЦІЯ СТУДЕНТІВ")
    print("-" * 70)
    
    enrollment1 = manager.enroll_student(student1, course)
    enrollment2 = manager.enroll_student(student2, course)
    
    # 4. Додавання оцінок
    print("\n📝 ДОДАВАННЯ ОЦІНОК")
    print("-" * 70)
    
    manager.add_grade(enrollment1, 'Лабораторна 1', 85, 100, GradeType.ASSIGNMENT)
    manager.add_grade(enrollment1, 'Тест 1', 90, 100, GradeType.QUIZ)
    manager.add_grade(enrollment2, 'Лабораторна 1', 92, 100, GradeType.ASSIGNMENT)
    
    # 5. Демонстрація магічних методів
    print("\n🔮 МАГІЧНІ МЕТОДИ")
    print("-" * 70)
    print(f"Курс: {course}")  # __str__
    print(f"Модулів у курсі: {len(course)}")  # __len__
    print(f"Курсів у студента: {len(student1)}")  # __len__
    print(f"Фінальна оцінка: {enrollment1.calculate_grade():.2f}%")
    
    # 6. Ітерація по модулях
    print("\n📖 СТРУКТУРА КУРСУ")
    print("-" * 70)
    for i, module in enumerate(course, 1):  # __iter__
        print(f"{i}. {module.title} ({len(module)} уроків)")
        for lesson in module:
            print(f"   - {lesson.title}")
    
    # 7. Розклад
    print("\n📅 РОЗКЛАД")
    print("-" * 70)
    
    event = ScheduleEvent(
        'evt1',
        course,
        'Лекція: ООП в Python',
        datetime(2025, 11, 20, 10, 0),
        datetime(2025, 11, 20, 11, 30),
        'Аудиторія 305'
    )
    manager.add_schedule_event(event)
    
    # 8. Звіт по курсу
    print("\n📊 ЗВІТИ")
    print(manager.generate_course_report('CS101'))
    
    # 9. Експорт даних (Strategy Pattern - OCP)
    print("\n💾 ЕКСПОРТ ДАНИХ")
    print("-" * 70)
    
    # Експорт в JSON
    manager.export_students(JSONExportStrategy(), Path('students.json'))
    
    # Експорт в CSV
    manager.export_students(CSVExportStrategy(), Path('students.csv'))
    
    # Збереження всієї системи
    manager.save_to_json(Path('course_system.json'))
    
    print("\n" + "=" * 70)
    print("✅ ДЕМОНСТРАЦІЯ ЗАВЕРШЕНА")
    print("=" * 70)
    
    # Демонстрація SOLID принципів
    print("\n📌 РЕАЛІЗОВАНІ SOLID ПРИНЦИПИ:")
    print("✓ SRP: Кожен клас має одну відповідальність")
    print("✓ OCP: Можна додавати нові стратегії експорту без зміни коду")
    print("✓ LSP: Student/Instructor можуть замінити User")
    print("✓ ISP: Розділені інтерфейси (Serializable, Notifiable, Gradable)")
    print("✓ DIP: Залежності через абстракції (UserFactory, Strategy)")


if __name__ == "__main__":
    main()