# #4


while True:
        a = input('Введіть слово: ').strip().lower()
        b = input('Введіть слово: ').strip().lower()

        ok = True
        for ch in b:
            if a.find(ch) == -1:
                ok = False
                break

        print("Yes" if ok else "No")
        break


# a = input('Введіть слово: ')
# b = input('Введіть слово: ')
#
# for ch in b:
#     if a.count(ch) < b.count(ch):
#         print("Слово скласти не вийде!")
#         break
# else:
#     print('Слово можна скласти!')

#1
text = input("Введіть текст: ")

result = ""
for ch in text:
    if ch.isupper():
        result += "*"
    else:
        result += ch

print(result)
# #2

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

# #3
import string

# a. Символ, що трапляється найбільшу кількість разів

text = input("Введіть текст: ")
# text = "aaaaaa bbb cccc dddd gggggg "

result = []
max_digits = 0
while len(text):
    letter = ''
    for ch in text:
        if text.count(ch) >= max_digits:
            letter = ch
            max_digits = text.count(ch)
        else:
            text = text.replace(ch, '')
    if letter:
        text = text.replace(letter, '')
        result.append(letter)

print('Символи, що трапляється найбільшу кількість разів: ', result)

# b. Кількість знаків пунктуації
punct_count = sum(1 for ch in text if ch in string.punctuation)
print("b. Кількість знаків пунктуації:", punct_count)

# c. Літери алфавіту, що не були знайдені у тексті
ukrainian_alphabet = "абвгґдежзийіїклмнопрстуфхцчшщьюя"

text = input("Введіть рядок: ").lower()

missing_letters = ""

for letter in ukrainian_alphabet:
    if letter not in text:
        missing_letters += letter

print("Літери, що не зустрілися у тексті:", missing_letters)

# d. Кількість унікальних символів (ті, що зустрічаються лише один раз)
unique_count = sum(1 for ch in text if text.count(ch) == 1)
print("d. Кількість унікальних символів:", unique_count)
# #5
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
#


