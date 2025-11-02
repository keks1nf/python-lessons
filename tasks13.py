
class Counter:  # при ітерації лічильник видає значення від 1 до max_value
    def __init__(self, max_value: int):
        self.value = 1
        self.max_value = max_value

    def __iter__(self):
        self.value = 1
        return self  # в якості ітератору повертаємо себе

    def __next__(self):  # буде спрацьовувати, коли Python буде просити елемент
        if self.value > self.max_value:
            raise StopIteration

        return_value = self.value
        self.value += 1

        return return_value


counter = Counter(100)

print('Цикл 1')
for el in counter:
    print(el)

print('Цикл 2')
for el in counter:
    print(el)

print('Цикл 3')
for el in counter:
    print(el)
