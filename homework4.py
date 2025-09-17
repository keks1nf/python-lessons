#1
number = int (input("Enter a number: "))

if number % 2 == 0:
  print(f" {number} is an even number.")
else:
  print(f"{number} is an odd number.")
#2
day_of_week = input("Enter a day of week: ")
if day_of_week == "1":
    print('Monday')
elif day_of_week == "2":
    print('Tuesday')
elif day_of_week == "3":
    print('Wednesday')
elif day_of_week == "4":
    print('Thursday')
elif day_of_week == "5":
    print('Friday')
elif day_of_week == "6":
    print('Saturday')
elif day_of_week == "7":
    print('Sunday')
else:
    print("Sorry, I don't understand that.")

#a
day_of_week_1 = input("Enter a day of week: ")
match day_of_week_1:
    case "1":  # if можна додати
        print('Monday')
    case "2":
        print('Tuesday')
    case "3":
        print('Wednesday')
    case "4":
        print('Thursday')
    case "5":
        print('Friday')
    case "6":
        print('Saturday')
    case "7":
        print('Sunday')
    case _:  # аналог else
        print("Sorry, I don't understand that.")
#b
month = int(input("Enter a month: "))
match month:
    case 12| 1 | 2:
        print('Winter')
    case 3 | 4 | 5:
        print('Spring')
    case 6 | 7 | 8:
        print('Summer')
    case 9 |10 | 11:
        print('Fall')
    case _:
        print('Not a month')


#3
name = input("Enter your name: ")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f'Hello {name}')
elif number % 2 == 1 and number % 3 == 0:
    print(f'{number * number}')
else:
    print(f'Bye')
#4
number = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
mod_result = number % number2
result = number / number2
if mod_result == 0:
    print(f"Integer {int(result)}")
else:
    print(f"{result:.2f}")
#
'''
кор вводить 6 значне число 
яке число щасливим
щасливе сума перших трьох дорівнює сумі останіх трьох 
'''
# if len(number) != 6:
#     print("Sorry, I don't understand that.")
# elif  # перевірка на щасливе
# else # не щасливе

number = input('Введіть шестизначне число: ')

if len(number) == 6:
    first_sum = int(number[0]) + int(number[1]) + int(number[2])
    last_sum = int(number[3]) + int(number[4]) + int(number[5])

    if first_sum == last_sum:
        print('Число є щасливим!)')
    else:
        print('Число звичайне(')
else:
    print('Ви ввели не шестизначне число!')

'''
Користувач ввод день року (1-365)
Скажіть який це день тижня, знаючи що 1 день - це понеділок
'''

day_number = int(input("Введіть день року (1-365): "))

# список днів тижня
week_days = ["Понеділок", "Вівторок", "Середа", "Четвер",
             "П’ятниця", "Субота", "Неділя"]

# індекс дня (зсув -1, бо 1-й день = 0-й індекс)
day_of_week = week_days[(day_number - 1) % 7]

print("Це:", day_of_week)




'''
Користувач день року(1-365).
Скажіть, який це день тижня, знаючи, що 1 день - це понеділок.
'''

day = int(input('Введіть день року(1-365): '))

if 1 <= day <= 365:
    match day % 7:
        case 0:
            print('Неділя')
        case 1:
            print('Понеділок')
        case 2:
            print('Вівторок')
        case 3:
            print('Середа')
        case 4:
            print('Четвер')
        case 5:
            print('П`ятниця')
        case 6:
            print('Субота')
else:
    print('Такого дня не існує в році!')


#11
text = input("Введіть текст: ")
numbers = set("0123456789")

if set(text) & numbers:
    print("У тексті є цифри.")
else:
    print("Цифр немає.")



