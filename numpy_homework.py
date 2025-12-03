import numpy as np

# 1
arr1 = np.arange(1, 101)
print(arr1)
# 2
arr3d = np.random.randint(1, 100, (3, 4, 5))
odd_numbers = arr3d[arr3d % 2 == 1]
print(odd_numbers)
# 3
arr2 = np.arange(1, 17).reshape(4, 4)
transposed = arr2.T

print(arr2)
print(transposed)
# 4
arr_rand = np.random.randint(0, 101, 100)
greater_50 = arr_rand[arr_rand > 50]

print(greater_50)
