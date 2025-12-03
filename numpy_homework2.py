import numpy as np

np.random.seed(42)  # відтворювання даних

#  масив

days = 5
groups = 3

# занять 2–5
lessons = np.random.randint(2, 6, size=(days, groups))

#  відвідування
attendance = np.array([
    [np.random.randint(0, lessons[d, g] + 1) for g in range(groups)]
    for d in range(days)
])

# об'єднання
data = np.stack([lessons, attendance], axis=2)

print(f"масив (день, група, [занять, відвідувань]):\n")
print(data)

mean_lessons = np.mean(data[:, :, 0])  # 0
mean_visits = np.mean(data[:, :, 1])  # 1

print(f"Середня кількість занять за день: {mean_lessons: .2f}")
print(f"Середня кількість відвідувань:  {mean_visits: .2f}")

daily_visits = np.sum(data[:, :, 1], axis=1)

day_max = np.argmax(daily_visits)
day_min = np.argmin(daily_visits)

print(f"Максимальні відвідування в день №", day_max)
print(f"Мінімальні відвідування в день №", day_min)

total_lessons = np.sum(data[:, :, 0])
total_visits = np.sum(data[:, :, 1])

attendance_percent = total_visits / total_lessons * 100

print(f"Загальний відсоток відвідуваності: {attendance_percent: .2f}")
