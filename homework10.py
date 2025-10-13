#1.
text = input('Введіть рядок: ').split()

freq = {}

for w in text:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)
#2
nums = list(map(int, input('Введіть числа через пробіл: ').split())) #2 5 8 9 4 78 7 1
for num in range(0, len(nums)):
    if len(nums) >= 3:
        nums.pop(2)
        print(nums)
    else:
        nums.pop(0)
        print(nums)
#3
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'.lower()
result = ''
for ch in text:
    if ch in morze:
        result += f' {morze[ch]}'
    elif ch == " ":
        result += ' /'
print("Текст у коді Морзе:", result.strip())




