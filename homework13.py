#1-2
class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"{self.name} — середній бал: {self.average_grade():.2f}"


class StudentGroup:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def best_student(self) -> Student | None:
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average_grade())

    def __iter__(self):
        return iter(self.students)

    def __str__(self):
        return f"Група '{self.group_name}' — кількість студентів: {len(self.students)}"



s1 = Student("Іван", [90, 85, 88])
s2 = Student("Марія", [95, 100, 98])
s3 = Student("Олег", [70, 75, 80])

group = StudentGroup("DA 10")

group.add_student(s1)
group.add_student(s2)
group.add_student(s3)

print(group)
print("\nУсі студенти:")
for student in group:
    print(student)

best = group.best_student()
if best:
    print(f"\nНайуспішніший студент: {best.name} (середній бал: {best.average_grade():.2f})")


#3
class BankAccount:
    def __init__(self, account: str, balance: float):
        self.account = account
        self.balance = balance

    def __str__(self):
        return f"Власник: {self.account}. Баланс: {self.balance:.2f}"

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Сума повинна бути більшою за 0.")
        elif amount > self.balance:
            print("Недостатньо коштів.")
        else:
            self.balance -= amount
            print(f"Знято {amount:.2f}. Новий баланс: {self.balance:.2f}")

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено {amount:.2f}. Новий баланс: {self.balance:.2f}")
        else:
            print("Сума повинна бути більшою за 0.")

    def get_balance(self):
        return self.balance



acc = BankAccount('Vik', 50000)
print(acc)
acc.withdraw(100)
acc.deposit(500)
print(f"Поточний баланс: {acc.get_balance():.2f}")



