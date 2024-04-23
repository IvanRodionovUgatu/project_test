class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


r1 = Rectangle(12, 5)
print(f'Площадь: {r1.square()}')
print(f'Периметр: {r1.perimeter()}')