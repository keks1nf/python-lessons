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
