class Human:
    def __init__(self, name, city, year_birth):
        self.name = name
        self.city = city
        self.year_birth = year_birth

    def __str__(self):
        return f'Человек с именем {self.name}, из города {self.city}, {self.year_birth} года рождения'


h1 = Human('ivan', 'ufa', 2004)
print(str(h1))