import numpy as np

np.random.seed(100_000)

array = np.random.randint(-100, 100, size=(5, 5))

print(array)
print('*' * 24)

# -----Зрізи
print(array[1, 0])  # звернення по індексу (можна через кому)
print(array[:3])  # зріз перших 3-х рядків
print(array[:3, :3])  # перші 3 рядки, та 3 колонки
print(array[:, ::2])  # всі рядки, кожна друга колонка
print(array[1:4, 1:4])  # рівно центр масиву

# -----Булеві маски
mask = array[:, 0] > 30  # всі рядки, у яких перший елемент(колонка) > 30

print(mask)
print(array[mask])

array[array < 0] = 0  # заміна всіх від'ємних значень на 0
print(array)

# -----Індекси
print(array[[0, 3, 4]])  # 0, 3 та 4 рядок (обов'язково в [])
print(array[[0, 3, 4], [1, 2, 4]])  # перетин

# -----Перетворення
a = np.array([1, 2, 3, 4, 5, 6])

# -----Робота з np.nan

array = np.array([1, np.nan, 2, 3, 4, np.nan, np.nan, 8, 9])
array = np.reshape(array, (3, 3))

# print(np.isnan(array))  # знаходження всіх nan

# array[np.isnan(array)] = 0  # заміна nan на 0


# print(np.nan_to_num(array, nan=np.nanmean(array)))  # те саме, тільки повертає результат

# print(array)
# print(np.nansum(array))

# -----where
c = np.array([19, -3, 5, 8, 10, 0])

print(c[np.where(c > 5)])

print(np.where(c < 5, 100, 0))

c = c.reshape((2, 3))
print(c)
print(np.where(c > 5))
