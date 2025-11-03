#1
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: {self.price} грн"


class Shop:
    def __init__(self, name: str):
        self.name = name
        self.products: list[Product] = []

    def add_product (self, product: Product) -> None:
        self.products.append(product)
        print(f'Продукт {product.name} додано до магазину {self.name}')

    def show_products(self) -> None:
        if not self.products:
            print("Немає продуктів")
        else:
            print(f'Продукти в магазині {self.name}')
            for product in self.products:
                print(f"{product.name}: {product.price} грн.")

    def __contains__(self, item: str) -> bool:
        for p in self.products:
            if p.name.lower() == item.lower():
                return True
        return False

    def __str__(self) -> str:
        return f"Магазин {self.name} - кількість товарів {len(self.products)}"



shop = Shop("Продукти")

shop.add_product(Product("Хліб", 20))
shop.add_product(Product("Молоко", 30))
shop.add_product(Product("Яйця", 50))

shop.show_products()

print("print 'Хліб' in shop: ", 'Хліб' in shop)
print("print 'Масло' in shop: ", 'Масло' in shop)
print("print shop: ", shop)

#2
class Passenger:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def hi(self):
        print(f'Привіт! Мене звати {self.name}, мені {self.age} років')


class Auto:
    def __init__(self, name: str, max_passenger: int):
        self.name = name
        self.max_passenger = max_passenger
        self.passengers = []

    def __str__(self):
        return f'Авто {self.name} - кількість пасажирів {self.max_passenger}'

    def add(self, human: Passenger) -> None:
        if len(self.passengers) < self.max_passenger:
            self.passengers.append(human)
            print(f'Пасажир {human.name} сів у машину {self.name}')
        else:
            print(f'У машині {self.name} немає вільних місць')

    def __len__(self) -> int:
        return len(self.passengers)

    def show_passengers(self) -> None:
        if not self.passengers:
            print('Немає пасажирів')
        else:
             print(f'Пасажири в {self.name}')
             for human in self.passengers:
                 human.hi()

def __str__(self) -> str:
    return f'Машина {self.name} | Пасажирів: {len(self.passengers)}/{self.max_passengers}'

a1 = Auto("Audi", 4)
h1 = Passenger('Марія', 20)
h2 = Passenger("Петро", 20)
h3 = Passenger('Віктор', 20)
h4 = Passenger('ольга',25)
h5 = Passenger('Станіслав', 25)
a1.add(h1)
a1.add(h2)
a1.add(h3)
a1.add(h4)
a1.add(h5)

print(a1)
print(f"Кількість пасажирів: {len(a1)}")

a1.show_passengers()
