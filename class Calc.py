class Calc:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def exponentiate(self, a, b):
        return a ** b

    def integer_division(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b

    def remainder(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b
