class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            raise ZeroDivisionError
        return self.a / self.b


c1 = Calculator(10, 5)
print(f'Сложение: {c1.addition()}')
print(f'Вычитание: {c1.subtraction()}')
print(f'Умножение: {c1.multiplication()}')
print(f'Деление: {c1.division()}')