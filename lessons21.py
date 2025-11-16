class Calculator:
    @staticmethod
    def plus(a, b) -> int:
        return a + b

    @staticmethod
    def minus(a, b) -> int:
        return a - b

    @staticmethod
    def multiply(a, b) -> int:
        return a * b

    @staticmethod
    def divide(a, b) -> int:
        return a / b


calc = Calculator()
print(calc.plus(1, 2))
print(calc.minus(1, 2))


class Safe:
    def __init__(self, start_code: str, value: int) -> None:
        self.__code = start_code
        self.__value = value

    @property
    def code(self):  # геттер
        return self.__code

    @code.setter
    def code(self, new_code: str):  # сеттер
        self.__code = new_code


safe = Safe('12354', 0)
print(safe.code)
safe_code = '453454'
print(safe_code)
