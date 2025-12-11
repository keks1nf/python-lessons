import matplotlib.pyplot as plt

#
# '''
# Figure, Axes - два основних об'єкти
#
# Figure - основне вікно (полотно)
# Axes - графік, окреме "вікно" всередині Figure
# '''
#
# x1 = np.array([1, 3, 2, 1])
# y1 = np.array([1, 1, 5, 1])
#
# x2 = np.arange(1, 11)
# y2 = np.arange(21, 31)
#
# plt.plot([5, 2, 7], [10, 12, -1])
# plt.plot(x1, y1,
#          color='#00c2fc',
#          linestyle='-.',
#          marker='o',
#          markerfacecolor='red',
#          linewidth=3,
#          label='Моя красива лінія!')
#
# plt.plot(x2, y2, ':b')
#
# plt.title('Мій перший лінійний графік!')
# plt.xlabel('Ось X')
# plt.ylabel('Ось Y')
#
# plt.legend(loc='upper right')
#
# plt.show()


# # Кілька графіків (ручне створення)
#
# fig, ax = plt.subplots(2, 2)
#
# ax[0, 0].plot([1, 2, 3], [1, 2, 3])
# ax[0, 0].set_title("Перший")
#
# ax[0, 1].plot([5, 6, 7], [8, 1, -30])
# ax[0, 1].set_title("Другий")
#
# plt.show()


# Створення кількох графіків через plt

# plt.subplot(1, 3, 1)  # рядок, колонка, індекс (з 1-го)
# plt.plot([1, 2], [2, 3])
# plt.title('Перший графік')
#
# plt.subplot(1, 3, 2)  # рядок, колонка, індекс (з 1-го)
# plt.plot([10, 5], [-3, 0])
# plt.title('Другий графік')
#
# plt.subplot(1, 3, 3)  # рядок, колонка, індекс (з 1-го)
# plt.plot([1, 2, 3], [1, 0, 2])
# plt.title('Третій графік')
#
# plt.show()

# 1 Точковий графік

# fig, ax = plt.subplots(1, 2)
#
# x1 = np.random.rand(1000)
# y1 = np.random.rand(1000)
#
# ax[0].scatter(x1, y1)
# ax[0].set_title("Scatter Plot")
#
# x2 = np.random.normal(loc=0, scale=0.5, size=1000)
# y2 = np.random.normal(loc=0, scale=0.5, size=1000)
# ax[1].scatter(x2, y2)
# ax[1].set_title("Normal Plot")

# 2 Стовбчата діаграма(потребує категорій)
#
# age = [10, 3, 24, 25, 31]
# names = ['bob', 'alice', 'rob', 'john', 'jim']
#
# plt.bar(names, age, color=['r', 'g', 'b', 'y', 'c'], edgecolor='black', width=0.5)

# 3 Гістограма
# fig, ax = plt.subplots(1, 2)
#
# x1 = np.random.rand(1000)
# ax[0].hist(x1, 100)
# x2 = np.random.normal(0, 0.5, 1000)
# ax[1].hist(x2, 100)

# 4 Boxplot
# x1 = np.random.rand(1000)
# x2 = np.random.normal(0, 0.5, 1000)
# plt.boxplot((x1, x2))

# 5 pie chart
salary = [10000, 15000, 15000, 7000, 150, 54000]
names = ["bob", "cdf", "sie", "val", "jim", "alice"]
plt.pie(salary, labels=names, autopct="%1.1f%%")

plt.show()
