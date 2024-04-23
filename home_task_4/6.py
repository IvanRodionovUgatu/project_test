#Множественное наследование
class Dad:
    def dad_genes(self):
        return 'Гены отца'


class Mam:
    def mam_genes(self):
        return 'Гены матери'


class Child(Dad, Mam):
    def life(self):
        return 'Зарождение жизни'


#Миксины
class Mixin:
    def mixin_method(self):
        return "Метод Mixin"


class TestClass(Mixin):
    pass


t1 = TestClass()
print(t1.mixin_method())
