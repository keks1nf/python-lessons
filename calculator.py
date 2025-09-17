number_1 = float(input('Enter a number: '))
operation = input('Enter an operation (+, -, *, /): ')
number_2 = float(input('Enter another number: '))

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    if number_2 != 0:
        result = number_1 / number_2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

print("Result:", result)

#pass заглушка