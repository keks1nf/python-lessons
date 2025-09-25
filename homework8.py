# #4
import sys

while True:
        a = input('Введіть слово: ').strip()#.lower()
        b = input('Введіть слово: ').strip()#.lower()

        ok = True
        for ch in b:
            if a.find(ch) == -1:
                ok = False
                break

        print("Yes" if ok else "No")
        break

sys.exit(0)
# # #1
# text = input("Введіть текст: ")

# result = ""
# for ch in text:
#     if ch.isupper():
#         result += "*"
#     else:
#         result += ch

# print(result)
#2


# lines = []  # ??????
# while True:
#     s = input().strip()
#     if not s:
#         break
#     lines.append(s)



lines = [
    1001,
    100001001010,
    1000001,
]

for digits in lines:
    max_zeros = 0
    count = 0

    for ch in str(digits):
        if ch == '0':
            count += 1
            
            if count > max_zeros:
                max_zeros = count
        else:
            count = 0
    print('max zeros', max_zeros)

#3
import string

text = input("Введіть текст: ")

# a. Символ, що трапляється найбільшу кількість разів
#???

# b. Кількість знаків пунктуації
punct_count = sum(1 for ch in text if ch in string.punctuation)
print("b. Кількість знаків пунктуації:", punct_count)

# c. Літери алфавіту, що не були знайдені у тексті
#???

# d. Кількість унікальних символів (ті, що зустрічаються лише один раз)
unique_count = sum(1 for ch in text if text.count(ch) == 1)
print("d. Кількість унікальних символів:", unique_count)
#5
text = input("Введіть рядок: ")

if not text:
    print("")
else:
    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += text[i-1] + str(count)
            count = 1

    result += text[-1] + str(count)

    print("Закодований рядок:", result)



