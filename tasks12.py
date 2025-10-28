
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def show(self):
        print(f"Point({self.x}, {self.y})")



p = Point(2, 3)
p.move(1, -1)
p.show()


class CoffeeMachine:
    def __init__(self, water: int, coffee: int, milk: int):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def __check(self, need_water=0, need_coffee=0, need_milk=0):
        if self.water < need_water:
            print(" Не вистачає води!")
            return False
        if self.coffee < need_coffee:
            print(" Не вистачає кави!")
            return False
        if self.milk < need_milk:
            print(" Не вистачає молока!")
            return False
        return True

    def make_espresso(self):
        if self.__check(30, 20):
            self.water -= 30
            self.coffee -= 20
            print("Еспресо!")

    def make_latte(self):
        if self.__check(30, 20, 50):
            self.water -= 30
            self.coffee -= 20
            self.milk -= 50
            print("Лате")

    def refill(self, water=0, coffee=0, milk=0):
        self.water += water
        self.coffee += coffee
        self.milk += milk
        print(" Поповнення виконано!")

    def status(self):
        print(f"Залишки: water={self.water}ml, coffee={self.coffee}g, milk={self.milk}ml")

cm = CoffeeMachine(100, 60, 100)
cm.status()

cm.make_espresso()
cm.make_latte()
cm.status()

cm.refill(water=100, milk=100)
cm.status()


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print(f"Книга '{title}' вже є в бібліотеці!")
        else:
            self.books[title] = author
            print(f"Додано книгу: '{title}' - {author}")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Книга '{title}' видалена.")
        else:
            print(f" Книга '{title}' відсутня!")

    def find_by_title(self, title):
        if title in self.books:
            print(f" Знайдено: '{title}' - {self.books[title]}")
        else:
            print(" Такої книги немає.")

    def find_by_author(self, author):
        pass

    def show_books(self):
        if not self.books:
            print(" Бібліотека порожня.")
        else:
            print(" Список книг:")
            for title, author in self.books.items():
                print(f"• '{title}' - {author}")


lib = Library()

lib.add_book("1984", 'Джордж Орвелл')
lib.add_book("Тіні забутих предків", "Михайло Коцюбинський")
lib.add_book('Старий і море', 'Ернест Гемінґвей')


lib.show_books()

lib.find_by_title("Тіні")

lib.remove_book("Тіні")
lib.show_books()
