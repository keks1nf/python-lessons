# #1
count = 0

for number in range(100, 1000):
    a = number // 100
    b = (number // 10) % 10
    c = number % 10

    if a == b or a == c or b == c:
        count += 1

print("Кількість чисел з двома однаковими цифрами:", count)

count = 0
for number in range(100, 1000):
    number_str = str(number)
    uniq_digits = ''

    for digit in number_str:
        if digit not in uniq_digits:
            uniq_digits += digit

    if len(uniq_digits) <= 2:
        count += 1

print(count)

# #2
numbers = range(2, 101)
result = 0

for number1 in numbers:
    is_prime = True
    for number2 in range(2, number1):
        if number1 % number2 == 0:
            is_prime = False
            break
    if is_prime:
        result += 1

print(result)
print("Кількість простих чисел:", (result))
#3
text = input("Число: ")

number = ""
for ch in text :
    if ch != "6" and ch != "3":
        number += ch
print(number)
#4
start_range = int(input('Початок діапазону: '))
end_range = int(input('Кінець діапазону: '))

while True:
    users_number = int(input("Число: "))
    if start_range <= users_number <= end_range:
        print("Успіх! Число в діапазоні:", users_number)
        memory = ''
        for number in range(start_range, end_range+1):
            if users_number == number:
                number = f'!{number}!'

            memory = f'{memory} {number}'
        print(memory)
        break
    else:
        print("Спробуй ще")

#5
start_range = int(input("Початок діапазону: "))
end_range = int(input("Кінець діапазону: "))

for x in range(start_range, end_range + 1):
    print(f"Таблиця множення для {x}:")
    memory = ""

    for y in range(1, 11):
        memory = f"{memory} {x} × {y} = {x * y}"

    print(memory)
    print('-' * len(memory))










