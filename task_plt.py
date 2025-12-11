import matplotlib.pyplot as plt

# 1
plt.plot([1, 4], [1, 1], color='red')
plt.plot([4, 4], [1, 3], color='green')
plt.plot([4, 1], [3, 3], color='blue')
plt.plot([1, 1], [3, 1], color='orange')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# 2
weight = [50, 55, 60, 65, 65, 70, 73, 75, 80, 83, 85, 90]
height = [155, 160, 160, 165, 170, 170, 173, 175, 180, 180, 183, 185]

plt.scatter(weight, height)

plt.xlabel("Вага")
plt.ylabel("Зріст")
plt.title("Залежність ваги від зросту")
plt.show()

# 3
ages = [12, 13, 13, 14, 15, 17, 12, 16, 18, 50]

plt.boxplot(ages)

plt.xlabel("Вік")
plt.title("Boxplot (медіана та викид)")
plt.show()

# 4
ages = [12, 13, 13, 14, 15, 17, 12, 16, 18, 50]

more_ages = [20, 21, 22, 23, 24, 25, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
ages.extend(more_ages)

plt.hist(ages, bins='auto', color='skyblue', edgecolor='black')
plt.title('Гістограма віку')
plt.xlabel('Вік')
plt.ylabel('Кількість')

plt.show()
