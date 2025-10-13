double_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(len(double_list)) # 3
print(double_list[1]) #[4, 5, 6]
print(double_list[1][0]) #4 двомірний список [ряд] [колонка]

for num in double_list:
    for num2 in num:
        print(num2, end=' ')
    print()



for row_index in range(0, len(double_list)):
    for col_index in range(0, len(double_list[row_index])):
        print(double_list[row_index][col_index], end=' ')
    print()
