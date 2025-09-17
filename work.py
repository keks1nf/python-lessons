#5
text = input("Введіть текст: ")
n = int(input("Введіть число: "))
print(text * n)
#6
num = int(input("Введіть число: "))
print(-num)
#7
name = input("Введіть ваше ім’я: ")
print(f"Привіт, {name}!")
#8
text = "Сьогодні середа."
word = input("Введіть слово для пошуку: ")

if word in text:
    print("Слово знайдено!")
else:
    print("Слова немає.")
#9
bullets = int(input("Кількість патронів: "))
enemies = int(input("Кількість ворогів: "))

need = enemies * 15

if bullets >= need:
    print("Патронів вистачить!")
else:
    print("Патронів не вистачить!")
#10
fuel = float(input("Кількість пального (л): "))
consumption = float(input("Витрата (л/100км): "))
distance = float(input("Відстань (км): "))

possible = (fuel / consumption) * 100

if possible >= distance:
    print("Пального вистачить!")
else:
    print("Пального не вистачить!")
#11
text = input("Введіть текст: ")

if ('0' in text
        or '1' in text
        or '2' in text
        or '3' in text
        or '4' in text
        or '5' in text
        or '6' in text
        or '7' in text
        or '8' in text
        or '9' in text
):
    print("У тексті є цифри.")
else:
    print("Цифр немає.")
#12
year = int(input("Введіть рік: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Цей рік високосний")
else:
    print("Цей рік не високосний")


