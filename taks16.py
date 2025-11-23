# class BankAccount:
#     def __init__(self, balance: float, daily_limit: float = 5000):
#         self._balance = balance
#         self._daily_limit = daily_limit
#         self._withdrawn_today = 0
#
#     def deposit(self, amount: float):
#         if amount <= 0:
#             raise ValueError("Сума поповнення повинна бути більшою за 0.")
#         self._balance += amount
#
#     def withdraw(self, amount: float):
#         if amount <= 0:
#             raise ValueError("Сума зняття повинна бути більшою за 0.")
#         if amount > self._balance:
#             raise ValueError("Недостатньо коштів на рахунку.")
#         if self._withdrawn_today + amount > self._daily_limit:
#             raise ValueError("Перевищено ліміт зняття.")
#         self._balance -= amount
#         self._withdrawn_today += amount
#
#     def get_balance(self):
#         return self._balance
#
#     def reset_daily_limit(self):
#         self._withdrawn_today = 0


# class Safe:
#     def __init__(self, code, content):
#         self.__code = code
#         self.__content = content
#         self.__is_open = False
#         self.__attempts = 3
#         self.__retries = 3
#
#     def open(self, code):
#         if self.__code == code:
#             self.__is_open = True
#             return self.__content
#         else:
#             return None
#
#     def change_code(self, old_code, new_code):
#         if self.__attempts == 0:
#             self.__retries -= 1
#             print(f"Заблоковано")
#             if self.__retries == 0:
#                 self.__reload_attempts()
#                 self.__reload_retries()
#         else:
#             if self.__code == old_code:
#                 self.__reload_attempts()
#                 self.__reload_retries()
#                 self.__code = new_code
#             else:
#                 self.__attempts -= 1
#
#     def put(self, item):
#         if self.__is_open:
#             self.__content = item
#         else:
#             raise RuntimeError(f'Сейф зачинено')
#
#     def __reload_attempts(self):
#         self.__attempts = 3
#
#     def __reload_retries(self):
#         self.__retries = 3
#
#
# acc = Safe("acc", "acc")
# acc.open("acc")
# acc.put(1)
# print(vars(acc))
# acc.change_code("acc", ".env")
# print(vars(acc))
# acc.change_code("acc", ".env")
# acc.change_code("acc", ".env")
# acc.change_code("acc", ".env")
# acc.change_code("acc", ".env")
# print(vars(acc))
# acc.change_code("acc", ".env")
# acc.change_code("acc", ".env")
# print(vars(acc))

# class Drone:
#     def __init__(self, fuel, ammo):
#         self.__fuel = fuel
#         self.__ammo = ammo
#         self.distance = 0
#
#     def fly(self, distance):
#         if distance <= 0:
#             return
#
#         fuel_ned = distance * 2
#         if self.__fuel >= fuel_ned:
#             self.__fuel -= fuel_ned
#             self.distance += distance
#             print(f'Залишок {self.__fuel}')
#         else:
#             print(f'Недостатньо палива')
#
#     def shoot(self, amount: int):
#         if self.__ammo >= amount:
#             self.__ammo -= amount
#             print(f'Залишок {self.__ammo}')
#         else:
#             print(f'Недостатньо боєприпасів')
#
#     def refuel(self, amount: int):
#         self.distance += amount
#         print(f'Паливо після заправки {self.__fuel}')
#
#     def reload(self, amount: int):
#         self.__ammo += amount
#         print(f'Боєприпаси після перезарядки {self.__ammo}')
#
#     def status(self):
#         print('---Статус дрона---')
#         print(f'Кількість палива {self.__fuel}')
#         print(f'Кількість боєприпасів {self.__ammo} ')
#         print(f'Пройдена відстань {self.distance} км')
#
#
# d = Drone(100, 50)
#
# d.status()
# d.fly(20)
# d.shoot(10)
# d.refuel(30)
# d.reload(20)
# d.status()
