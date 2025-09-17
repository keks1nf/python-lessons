
#1
correct_login = "admin"
correct_password = "12345"

# користувач вводить дані
login = input("Enter login: ")
password = input("Enter password: ")

if login == correct_login and password == correct_password:
    print("Password accepted.")
else:
    print("Sorry, that is the wrong login or password.")

login = input('Login: ')
password = input('Password: ')

# 1.
if login == 'admin' and password == 'qwerty123':
    print('WELCOME!')
else:
    print('Incorrect data!')

# 2.
if login == 'admin':
    if password == 'qwerty123':
        print('WELCOME!')
    else:
        print('Incorrect password!')
else:
    print('Incorrect login!')

# 3.
if login != 'admin':
    print('Incorrect login!')
elif password != 'qwerty123':
    print('Incorrect password!')
else:
    print('WELCOME!')



#2
temperature = float(input("Enter temperature: "))

if temperature <= 0:
    print("A cold, isn't it?")
elif temperature > 0 and temperature < 10: # 0 < temp > 10, temp < 10
    print("Cool.")
else:
    print("Nice weather we're having.")
#3
score1 = int(input("Кількість балів: "))
score2 = int(input("Кількість балів: "))
score3 = int(input("Кількість балів: "))

average = (score1 + score2 + score3) / 3

print(f"{round(average,2)}")

if average > 95:
    print("Congratulations! That is a great average!")



