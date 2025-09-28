#1
import random

nums = [random.randint(-20, 20) for _ in range(20)]
print("Список:", nums)


min_val = min(nums)
max_val = max(nums)


negatives = sum(1 for x in nums if x < 0)
positives = sum(1 for x in nums if x > 0)
zeros = nums.count(0)

print("Мінімальний елемент:", min_val)
print("Максимальний елемент:", max_val)
print("Кількість від'ємних:", negatives)
print("Кількість додатних:", positives)
print("Кількість нулів:", zeros)

#2
#import random
#
# random_word_list = random.sample(available_words, 10)
#
# print(random_word_list)
#
available_words = ['авокадо', 'айва', 'Аґрус', 'ананас', 'Апельсин', 'арбуз', 'банан', 'Груша', 'гранат', 'журавлина', 'зизифус', 'Інжир', 'кавун', 'киві', 'Кокос', 'ківі', 'кумкват', 'Лайм', 'лимон', 'Малина', 'манго', 'Маракуйя', 'диня', 'Мушмула', 'нектарин', 'Ожина', 'папайя', 'пасифлора', 'Персик', 'Пітахайя', 'порічка', 'Слива', 'смородина', 'суниця', 'тутовник', 'хурма', 'Черімойя', 'черешня', 'Чорниця', 'шовковиця', 'Яблуко']

filtered_words = [w for w in available_words if w[0].isupper()]

print(f'Cлова, що починаються з великої літери', filtered_words)
#3
import random

my_list = [random.randint(0, 50) for _ in range(50)]
print(my_list)

memory= []
for num in my_list:
    count = my_list.count(num)
    if count % 2 != 0 and memory.count(num) == 0:
        memory.append(num)
print(f'Числа, що з’являється непарну кількість разів: ', memory)
#4
types_list = [1,2,3, 3.12, 3.14, 5.54, True, False, 'fgfdghf', 'fgfgfgh', 'ghghgfhfgh' ]

list_int = []
list_str = []
list_bool = []
list_float = []
for ch in types_list:
    if type(ch) == int:
        list_int.append(ch)
    elif type(ch) == str:
        list_str.append(ch)
    elif type(ch) == bool:
        list_bool.append(ch)
    elif type(ch) == float:
        list_float.append(ch)
    else:
        print(f"Type Error", ch)
        exit()
print(f'Тип даних int: ', list_int)
print(f'Тип даних str: ',list_str)
print(f'Тип даних bool: ',list_bool)
print(f'Тип даних float: ',list_float)
#5

list1 = list(map(int, input("Введіть перший список чисел через пробіл: ").split()))
list2 = list(map(int, input("Введіть другий список чисел через пробіл: ").split()))
print(list1)
print(list2)

if len(list1) != len(list2):
    print(f"Списки мають бути однакової довжини!")
else:
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    print(f"Результат:", result)

