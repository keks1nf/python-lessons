# #1
s = input("Введіть рядок: ")

upper = 0
lower = 0
spaces = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch == " ":
        spaces += 1

print("Upper", upper)
print("Lower", lower)
print("Spaces", spaces)
# #2
s = input("Введіть рядок: ")

letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)
# #3
s = input("Введіть рядок: ")
n = int(input("Введіть n: "))

result = s[:n].upper() + s[n:]
print(result)
# #4
s = input("Введіть рядок: ")

result = " ".join(s.split())

print(result)
# #5
s = input("Введіть рядок: ").strip()

if len(s) > 1:
    new_s = s[-1] + s[1:-1] + s[0]
else:
    new_s = s

print("Результат:", new_s)


#6
s = input("Введіть рядок: ") #TheOldSeaDogAtTheAdmiralBenbow

result = ""
for ch in s:
    if ch.isupper() and result:
        result += " " + ch
    else:
        result += ch

print(result)


