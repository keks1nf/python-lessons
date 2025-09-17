'''
Проблеми, які вирішують цикли:
1. Дублювання коду;
2.Ітерація

'''
# while поки є умова роботи

# counter = 1
# # 1 крок циклу - 1 повне виконання його блоку (1 ітерація)
# while counter <= 100_000: # умова роботи циклу ( поки вона True ->  цикл триває)
#      print(counter)
#      counter += 1
#
# while True: # while True - нескінченний цикл
#     print(counter)
#     counter += 1
#     if counter > 100:
#         break  # вихід з циклу )одразу його закриває)


# text = input(': ')
#
# index = 0
# while 0 <= index < len(text):
#     print(text[index])
#     index += 1

#---- for  задачі с чііткою послідовністю (ДЛЯ <частина> з <послідовність>)
#
# for number in range(1, 11):
#     print(number)

text = input(': ')

# for index in range(len(text)):
#     print(text[index])

for char in text:  #доступ до кожного елемента
    print(char)





