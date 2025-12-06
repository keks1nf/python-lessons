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

# матриця (рядок — студент, стовпець — предмет)
grades = np.array([
    [90, 85, 78, 92],
    [55, 60, 48, 70],
    [100, 95, 98, 97],
    [40, 55, 60, 50],
    [75, 80, 72, 68]
])

# Середня оцінка по кожному студенту
avg_students = np.mean(grades, axis=1)

# Середня оцінка по кожному предмету
avg_subjects = np.mean(grades, axis=0)

# Студенти, у яких хоча б одна оцінка < 50
low_score_students = np.where(np.any(grades < 50, axis=1))[0]

# Студент з найвищим середнім балом
best_student_index = np.argmax(avg_students)
best_student_score = avg_students[best_student_index]

print("Середня оцінка по кожному студенту:", avg_students)
print("Середня оцінка по кожному предмету:", avg_subjects)
print("Студенти з оцінками < 50:", low_score_students)
print(f"Найкращий студент: #{best_student_index} із середнім балом {best_student_score}")

# У двовимірному масиві (матриці):
# axis=0 — діяти по стовпцях (вниз)
# axis=1 — діяти по рядках (впоперек)
