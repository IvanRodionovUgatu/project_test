class Human:
    def __init__(self, name, city, year_birth):
        self.name = name
        self.city = city
        self.year_birth = year_birth

    def age(self):
        return 2024 - self.year_birth


h1 = Human('ivan', 'ufa', 2004)
print(f'Возраст: {h1.age()}')