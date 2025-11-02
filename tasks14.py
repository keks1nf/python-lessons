class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} грн"


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, product):
        self.items[index] = product

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items


    def __str__(self):
        total = sum(p.price for p in self.items)
        return "\n".join(str(p) for p in self.items) + f"\nЗагалом: {total} грн"



cart = Cart()
cart.add(Product("Хліб", 20))
cart.add(Product("Молоко", 30))
print(cart)



class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Власник: {self.owner} | Баланс: {self.balance:.2f}"

    def __add__(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено {amount:.2f}. Новий баланс: {self.balance:.2f}")
        else:
            print("Сума повинна бути більшою за 0.")

    def __sub__(self, amount: float):
        if amount <= 0:
            print("Сума повинна бути більшою  0.")
        elif amount > self.balance:
            print("Недостатньо коштів.")
        else:
            self.balance -= amount
            print(f"Знято {amount:.2f}. Новий баланс: {self.balance:.2f}")

    def __call__(self, amount: float):
        print("Дозволяє викликати об’єкт як функцію")
        self.__sub__(amount)



acc = BankAccount("Alex", 1500)
print(acc)

acc + 500
acc - 300
acc(200)
print(acc)

