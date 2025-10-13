#1
def repeat_string(s: str, n: int) -> str:
    return s * n

s = input('Введіть рядок: ')
n = int(input('Введіть число: '))

print(repeat_string(s, n))
#2
def insert_string(base: str, insert: str) -> str:
    mid = len(base) // 2
    return base[:mid] + insert + base[mid:]

base = input('Перший рядок: ')
insert = input('Другий рядок: ')

print(insert_string(base, insert))

