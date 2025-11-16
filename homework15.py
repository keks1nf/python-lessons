class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    class Volvo(Vehicle):
        def __init__(self, name, price):
            super().__init__(name, price)
            self.volvo = price
           