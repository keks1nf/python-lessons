import json
import os
from datetime import datetime


class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def info(self):
        return f"Назва: {self.name} | Ціна: {self.price} | Кількість: {self.stock}"

    def sell(self, amount: int):
        if amount <= 0:
            print("Кількість має бути більшою за 0")
        elif amount > self.stock:
            print("Недостатньо товару на складі")
        else:
            self.stock -= amount
            print(f"Продано {amount} шт. | Залишок: {self.stock}")

    def to_dict(self):
        return {
            "type": "Product",
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Product(data["name"], data["price"], data["stock"])


class FoodProduct(Product):
    def __init__(self, name, price, stock, expiration_date):
        super().__init__(name, price, stock)
        self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()

    def isExpired(self):
        return datetime.now().date() > self.expiration_date

    def info(self):
        status = "Прострочене" if self.isExpired() else "Свіже"
        return f"{super().info()} | Термін придатності: {self.expiration_date} | Статус: {status}"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "FoodProduct"
        data["expiration_date"] = self.expiration_date.strftime('%Y-%m-%d')
        return data

    @staticmethod
    def from_dict(data):
        return FoodProduct(data["name"], data["price"], data["stock"], data["expiration_date"])


class ElectronicProduct(Product):
    def __init__(self, name, price, stock, guarantee):
        super().__init__(name, price, stock)
        self.guarantee = guarantee

    def info(self):
        return f"{super().info()} | Гарантія: {self.guarantee} міс."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "ElectronicProduct"
        data["guarantee"] = self.guarantee
        return data

    @staticmethod
    def from_dict(data):
        return ElectronicProduct(data["name"], data["price"], data["stock"], data["guarantee"])


class Store:
    def __init__(self, filename="store_data.json"):
        self.filename = filename
        self.products = []
        self.loadData()

    def addProduct(self, product):
        self.products.append(product)
        self.saveData()
        print(f"Товар '{product.name}' додано у магазин.")

    def showProducts(self):
        if not self.products:
            print("Магазин порожній.")
            return
        print("\n--- Товари в магазині ---")
        for p in self.products:
            print(p.info())

    def sellProduct(self, product_name, amount):
        for p in self.products:
            if p.name.lower() == product_name.lower():
                p.sell(amount)
                self.saveData()
                return
        print(f"Товар '{product_name}' не знайдено.")

    def searchProduct(self, product_name):
        for p in self.products:
            if p.name.lower() == product_name.lower():
                print("\nЗнайдено товар:")
                print(p.info())
                return p
        print(f"Товар '{product_name}' не знайдено.")
        return None

    def saveData(self):
        data = [p.to_dict() for p in self.products]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def loadData(self):
        if not os.path.exists(self.filename):
            print("Файл не знайдено. Створено новий магазин.")
            return

        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            if item["type"] == "FoodProduct":
                self.products.append(FoodProduct.from_dict(item))
            elif item["type"] == "ElectronicProduct":
                self.products.append(ElectronicProduct.from_dict(item))
            else:
                self.products.append(Product.from_dict(item))

        print("Дані магазину успішно завантажено.")

    def menu(self):
        while True:
            print("\n=== МАГАЗИН ===")
            print("1. Додати товар")
            print("2. Показати всі товари")
            print("3. Продати товар")
            print("4. Пошук товару")
            print("5. Вихід")

            choice = input("Ваш вибір: ")

            if choice == "1":
                self.addMenu()
            elif choice == "2":
                self.showProducts()
            elif choice == "3":
                name = input("Введіть назву товару: ")
                amount = int(input("Кількість для продажу: "))
                self.sellProduct(name, amount)
            elif choice == "4":
                name = input("Введіть назву товару для пошуку: ")
                self.searchProduct(name)
            elif choice == "5":
                print("Вихід із програми. Дані збережено.")
                self.saveData()
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def addMenu(self):
        t = input("Тип товару (food / electronic / other): ").strip().lower()
        name = input("Назва товару: ")
        price = float(input("Ціна: "))
        stock = int(input("Кількість: "))

        if t == "food":
            exp = input("Термін придатності (YYYY-MM-DD): ")
            product = FoodProduct(name, price, stock, exp)
        elif t == "electronic":
            guarantee = int(input("Гарантія: "))
            product = ElectronicProduct(name, price, stock, guarantee)
        else:
            product = Product(name, price, stock)

        self.addProduct(product)


if __name__ == "__main__":
    store = Store()
    store.menu()
