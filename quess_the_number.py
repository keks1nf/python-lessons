import random
import time


computer_number = random.randint(1, 10) #випадкове число
start_time = time.time() # початковий час
attempts = 0 # кількість спроб

while True:
    user_number = int(input('Я загадав число від 1 до 100, вгадай:'))
    attempts += 1
    diff = abs(computer_number - user_number)
    if computer_number == user_number:
        end_time = time.time()

        print(f"Молодець! Моє число дійсно {computer_number}")
        print(f"Ти вгадав за {attempts} спроб.")
        print(f"Час проходження {round(end_time-start_time,2)} сек.")


        agein = input(f'Продовжити Y/N: ' )
        if agein == 'Y':
            computer_number = random.randint(1, 100)  # випадкове число
            start_time = time.time()  # початковий час
            attempts = 0  # кількість спроб

        else:
            break
    else:
        if diff >= 50:
            print("Дуже холодно!")
        elif diff >= 20:
            print("Холодно")
        elif diff >= 10:
            print("Тепло")
        elif diff >= 5:
            print("Гаряче!")
        else:
            print("Дуже гаряче!")
