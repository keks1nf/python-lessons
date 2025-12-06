import numpy as np

# 1
arr = np.random.randint(1, 21, size=(4, 4))
print(arr)
# 2
arr = np.random.random((10, 10))

print("Mean:", arr.mean())
print("Min:", arr.min())
print("Max:", arr.max())
# 3
arr = np.random.randint(1, 50, size=(5, 5))
print(arr)

di3 = arr[arr % 3 == 0]
print("Числа, що діляться на 3:", di3)
# 4
salaries = [34000, 76000, 65000, 45000, 34000, 67000, 43000]

s = np.array(salaries)
print(s)

# Медіана
median = np.median(s)
print(median)

# Викид
clean = s[s <= 3 * median]
print(clean)

# Середнє та медіана «чистих»
mean_clean = np.mean(clean)
median_clean = np.median(clean)

# 25-й перцентиль
p25 = np.percentile(clean, 25)

# Відсоток співробітників нижче p25
percent_below_25 = (np.sum(clean < p25) / len(clean)) * 100

print("Очищені зарплати:", clean)
print("mean_clean:", mean_clean)
print("median_clean:", median_clean)
print("percent_below_25:", percent_below_25)

# Приклад матриці оцінок (рядок — студент, стовпець — предмет)
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
