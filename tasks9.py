# #1
# nums = [2, 5, 8, 3, 10, 15, 1]
#
# total_sum = sum(nums)
#
# product = 1
# for x in nums:
#     product *= x
#
# print("Сума:", total_sum)
# print("Добуток:", product)
#
# evens = [x for x in nums if x % 2 == 0]
# print("Парні:", evens)
#
# count_5 = sum(1 for x in nums if x > 5)
# print("Більше за 5:", count_5)

#2
text = input('Введіть рядок: ').split() #New Delhi New York Paris Prague Reykjavik
unique_words = []
for word in text:
    if word not in unique_words:
        unique_words.append(word)
print(len(unique_words))
# #3
# nums = list(map(int, input('Введіть числа через пробіл: ').split()))
#
# squares = []
# for x in nums:
#     squares.append(x**2)
#
# print(*squares)
#
# # #4
# nums = [3, 7, 2, 9, 12, 5]
#
# nums.append(100)
# print(nums)
#
# nums.insert(1, 50)
# print(nums)
#
# nums.remove(9)
# print(nums)
#
