from abc import ABC, abstractmethod


# === АБСТРАКЦІЯ ===
class Vehicle(ABC):
    def __init__(self, brand, model, year, price_per_day):
        self._brand = brand  # Інкапсуляція
        self._model = model
        self._year = year
        self._price_per_day = price_per_day
        self._is_rented = False

    @abstractmethod
    def vehicle_class(self):
        """Повертає клас авто"""
        pass

    @abstractmethod
    def info(self):
        """Повертає інформацію про авто"""
        pass

    def rent(self):
        if self._is_rented:
            print(f"{self._brand} {self._model} вже орендовано.")
        else:
            self._is_rented = True
            print(f"{self._brand} {self._model} успішно орендовано!")

    def return_vehicle(self):
        if not self._is_rented:
            print(f"{self._brand} {self._model} вже повернуто.")
        else:
            self._is_rented = False
            print(f"{self._brand} {self._model} повернено!")

    def is_available(self):
        return not self._is_rented

    def get_price(self):
        return self._price_per_day


# === Успадкування за класом авто (ПОЛІМОРФІЗМ) ===
class EconomyCar(Vehicle):
    def vehicle_class(self):
        return "Економ"

    def info(self):
        return f"[{self.vehicle_class()} клас] {self._brand} {self._model} ({self._year}) - {self._price_per_day} грн/день"


class StandardCar(Vehicle):
    def vehicle_class(self):
        return "Стандарт"

    def info(self):
        return f"[{self.vehicle_class()} клас] {self._brand} {self._model} ({self._year}) - {self._price_per_day} грн/день"


class BusinessCar(Vehicle):
    def vehicle_class(self):
        return "Бізнес"

    def info(self):
        return f"[{self.vehicle_class()} клас] {self._brand} {self._model} ({self._year}) - {self._price_per_day} грн/день"


# === Клас сервісу (ІНКАПСУЛЯЦІЯ) ===
class RentalService:
    def __init__(self):
        self.__vehicles = []  # Приватний список усіх авто

    def add_vehicle(self, vehicle: Vehicle):
        self.__vehicles.append(vehicle)
        print(f"Додано: {vehicle.info()}")

    def show_available(self):
        print("\n=== Доступні авто ===")
        available = [v for v in self.__vehicles if v.is_available()]
        if not available:
            print("Немає вільних авто.")
        else:
            for v in available:
                print(v.info())

    def rent_vehicle(self, model_name):
        for v in self.__vehicles:
            if v._model.lower() == model_name.lower():
                v.rent()
                return
        print(f"Автомобіль {model_name} не знайдено.")

    def return_vehicle(self, model_name):
        for v in self.__vehicles:
            if v._model.lower() == model_name.lower():
                v.return_vehicle()
                return
        print(f"Автомобіль {model_name} не знайдено.")

    def calculate_total(self, model_name, days):
        for v in self.__vehicles:
            if v._model.lower() == model_name.lower():
                total = v.get_price() * days
                print(f"Оренда {v._brand} {v._model} на {days} днів = {total} грн.")
                return
        print(f"Автомобіль {model_name} не знайдено.")


if __name__ == "__main__":
    service = RentalService()

    # Додаємо авто
    service.add_vehicle(EconomyCar("Toyota", "Yaris", 2020, 800))
    service.add_vehicle(StandardCar("Mazda", "6", 2021, 1200))
    service.add_vehicle(BusinessCar("BMW", "5 Series", 2022, 2500))

    # Показуємо доступні
    service.show_available()

    # Оренда
    service.rent_vehicle("Yaris")
    service.calculate_total("Yaris", 3)

    # Повернення
    service.return_vehicle("Yaris")

    # Спроба орендувати авто, якого немає
    service.rent_vehicle("Civic")
