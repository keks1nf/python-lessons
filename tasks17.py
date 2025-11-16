class Employee:
    def __init__(self, first_name: str, last_name: str, salary: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.salary = salary

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    @full_name.setter
    def full_name(self, value: str):
        full_name_items = value.split()
        self.__first_name = full_name_items[0]
        self.__last_name = full_name_items[1]

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        self.__salary = max(0.0, value)


employee1 = Employee('John', 'Doe', -1)
print(employee1.full_name)
print(employee1.salary)
employee1.full_name = 'John Smith'
print(employee1.full_name)


class Product:

    def __init__(self, name: str, price: float, discount: int):
        self.__name = name
        self.__price = price
        self.discount = discount

    @property
    def final_price(self):
        return self.__price * (1 - self.discount / 100)

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value: int):
        if value > 90:
            raise ValueError('Discount must be less than 90')
        self.__discount = value


prod = Product('Samsung', 20000, 10)
print(prod.final_price)
try:
    prod2 = Product('Samsung', 20000, 91)
    print(prod2.final_price)
except ValueError as e:
    print(e)

import json
import os


class AppConfig:
    def __init__(self, settings: dict):
        self.settings = settings

    @classmethod
    def load_from_file(cls, file_path: str):
        if not os.path.exists(file_path):
            default_settings = {
                "host": "localhost",
                "port": 8080,
                "debug": True
            }
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(default_settings, f, indent=4, ensure_ascii=False)
            print(f"Створено новий файл: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            settings = json.load(f)

        return cls(settings)

    def save(self, file_path: str):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4, ensure_ascii=False)
        print(f"Збережено в {file_path}")

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value


if __name__ == "__main__":
    config = AppConfig.load_from_file("config.json")

    print("Host:", config.get("host"))
    print("Port:", config.get("port"))
    print("Debug:", config.get("debug"))

    # Зміни
    config.set("debug", False)
    config.save("config.json")
