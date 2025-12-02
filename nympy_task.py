import numpy as np

temp = np.array([22.4, 22.5, np.nan, 22.7, np.nan, 22.8, 22.9])
print(temp)

clean_temp = temp[~np.isnan(temp)]
print(clean_temp)

'''
Q1 — 25-й перцентиль (нижня квартиль)
Q3 — 75-й перцентиль (верхня квартиль)
IQR = Q3 – Q1

Викиди — це значення, які лежать за межами:
нижня межа:
lower_bound=Q1−1.5⋅IQR
верхня межа:
upper_bound=Q3+1.5⋅IQR
Все, що нижче або вище цих меж — аномалія.
'''
# 2

salaries = np.array([30000, 32000, 34000, 35000, 37000,
                     40000, 42000, 45000, 50000, 700000, 1000])

# квартилі
Q1 = np.percentile(salaries, 25)
Q3 = np.percentile(salaries, 75)
IQR = Q3 - Q1
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

# Межі
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("lower_bound:", lower_bound)
print("upper_bound:", upper_bound)

# аномалії
outliers_mask = (salaries < lower_bound) | (salaries > upper_bound)
outliers = salaries[outliers_mask]
print("аномалії:", outliers)

# видалення аномалій
cleaned = salaries[~outliers_mask]
print("видалення аномалій:", cleaned)

# аномалії на медіану
median = np.median(salaries)
replaced = salaries.copy()
replaced[outliers_mask] = median
print("аномалії на медіану:", replaced)

# 3

# (дні × магазини)
sales = np.array([
    [100, 200, 150],
    [105, 205, 800],
    [98, 210, 160],
    [102, 190, 155],
    [500, 195, 158],
])

sales_clean = sales.copy()

rows, cols = sales.shape

for col in range(cols):
    column = sales[:, col]

    Q1 = np.percentile(column, 25)
    Q3 = np.percentile(column, 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # маска аномалій
    mask = (column < lower) | (column > upper)

    # замінити аномалії медіаною стовпця
    median = np.median(column)
    sales_clean[:, col][mask] = median

print("Оригінальна таблиця:\n", sales)
print("\nЗаміна аномалій на медіану:\n", sales_clean)
