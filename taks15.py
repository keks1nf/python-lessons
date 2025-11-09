import json
from datetime import datetime


class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def info(self):
        return f'Назва товару: {self.name} | Ціна: {self.price} | Кількість на складі: {self.stock}'

    def sell(self, amount: int):
        if amount <= 0:
            print('Кількість має бути більшою за 0')
        elif amount > self.stock:
            print('Недостатня кількість товару')
        else:
            self.stock -= amount
            print(f'Продано {amount} шт. | Залишок: {self.stock}')

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }


class FoodProduct(Product):
    def __init__(self, name: str, price: float, stock: int, expiration_date: str) -> None:
        super().__init__(name, price, stock)
        self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()

    def isExpired(self):
        return datetime.now().date() > self.expiration_date

    def info(self):
        status = "Прострочене" if self.isExpired() else "Свіже"
        return f"{super().info()} | Термін придатності: {self.expiration_date} | Статус: {status}"

    def to_dict(self):
        data = super().to_dict()
        data["expiration_date"] = self.expiration_date.strftime('%Y-%m-%d')
        return data


class ElectronicProduct(Product):
    def __init__(self, name: str, price: float, stock: int, guarantee: int) -> None:
        super().__init__(name, price, stock)
        self.guarantee = guarantee

    def info(self):
        return f"{super().info()} | Гарантія: {self.guarantee} міс."

    def to_dict(self):
        data = super().to_dict()
        data["guarantee"] = self.guarantee
        return data


class Store:
    def __init__(self, filename="store_data.json") -> None:
        self.filename = filename
        self.products = []
        self.loadData()

    def addProduct(self, product: Product):
        self.products.append(product)
        self.saveData()
        print(f'Товар доданий: {product.name}')

    def showProducts(self):
        if not self.products:
            print("Магазин порожній.")
            return

        print("\n=== Товари в магазині ===")
        for product in self.products:
            print(product.info())

    def sellProduct(self, product_name, amount: int):
        for p in self.products:
            if p.name.lower() == product_name.lower():
                p.sell(amount)
                self.saveData()
                return
        print(f'Продукт {product_name} не знайдено.')

    def searchProduct(self, product_name):
        for p in self.products:
            if p.name.lower() == product_name.lower():
                print(f'Товар {product_name} знайдено:')
                print(p.info())
                return p
        print(f'Товар {product_name} не знайдено.')
        return None

    def saveData(self):
        data = [p.to_dict() for p in self.products]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def loadData(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for item in data:
                if item['type'] == 'FoodProduct':
                    self.products.append(
                        FoodProduct(item['name'], item['price'], item['stock'], item['expiration_date']))
                elif item['type'] == 'ElectronicProduct':
                    self.products.append(
                        ElectronicProduct(item['name'], item['price'], item['stock'], item['guarantee']))
                else:
                    self.products.append(Product(item['name'], item['price'], item['stock']))
            print("Дані магазину завантажено.")
        except FileNotFoundError:
            print("ℹФайл не знайдено. Створено новий магазин.")


def main():
    shop = Store()

    while True:
        print("\n=== МАГАЗИН ===")
        print("1️ Додати товар")
        print("2️  Показати всі товари")
        print("3️  Продати товар")
        print("4️  Знайти товар")
        print("5️  Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            t = input("Тип товару (food / electronic / other): ").strip().lower()
            name = input("Назва: ")
            price = float(input("Ціна: "))
            stock = int(input("Кількість: "))

            if t == "food":
                exp = input("Термін придатності (YYYY-MM-DD): ")
                shop.addProduct(FoodProduct(name, price, stock, exp))
            elif t == "electronic":
                g = int(input("Гарантія (міс): "))
                shop.addProduct(ElectronicProduct(name, price, stock, g))
            else:
                shop.addProduct(Product(name, price, stock))

        elif choice == '2':
            shop.showProducts()

        elif choice == '3':
            name = input("Назва товару: ")
            amount = int(input("Кількість для продажу: "))
            shop.sellProduct(name, amount)

        elif choice == '4':
            name = input("Введіть назву товару для пошуку: ")
            shop.searchProduct(name)

        elif choice == '5':
            print("Збереження та вихід...")
            shop.saveData()
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
