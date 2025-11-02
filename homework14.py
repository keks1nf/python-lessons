#1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} грн"


class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product (self, product):
        self.products.append(product)
        print(f'Продукт {product.name} додано до магазину {self.name}')

    def show_products(self):
        if not self.products:
            print("Немає продуктів")
        else:
            print(f'Продукти в магазині {self.name}')
            for product in self.products:
                print(f"{product.name}: {product.price} грн.")

    def __contains__(self, item):
        for p in self.products:
            if p.name.lower() == item.lower():
                return True
        return False

    def __str__(self):
        return f"Магазин {self.name} - кількість товарів {len(self.products)}"



shop = Shop("Продукти")

shop.add_product(Product("Хліб", 20))
shop.add_product(Product("Молоко", 30))
shop.add_product(Product("Яйця", 50))

shop.show_products()

print('Хліб' in shop)
print('Масло' in shop)

print(shop)

#2
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self, age):
        print(f'Привіт! Мене звати {self.name}, мені {self.age} років')


class Auto:
    def __init__(self, name, max_passenger):
        self.name = name
        self.max_passenger = max_passenger
        self.passengers = []

    def __str__(self):
        return f'Авто {self.name} - кількість пасажирів {self.max_passenger}'

    def add(self, human):
        if len(self.passengers) < self.max_passenger:
            self.passengers.append(human)
            print(f'Пасажир {human.name} сів у машину {self.name}')
        else:
            print(f'У машині {self.name} немає вільних місць')

    def __len__(self):
        return len(self.passengers)

    def show_passengers(self):
        if not self.passengers:
            print('Немає пасажирів')
        else:
             print(f'Пасажири в {self.name}')
             for human in self.passengers:
                 human.hi(self)

def __str__(self):
    return f'Машина {self.name} | Пасажирів: {len(self.passengers)}/{self.max_passengers}'

a1 = Auto("Audi", 4)
h1 = Human('Марія', 20)
h2 = Human("Петро", 20)
h3 = Human('Віктор', 20)
h4 = Human('ольга',25)
h5 = Human('Станіслав', 25)
a1.add(h1)
a1.add(h2)
a1.add(h3)
a1.add(h4)
a1.add(h5)

print(a1)
print(f"Кількість пасажирів: {len(a1)}")

a1.show_passengers()







