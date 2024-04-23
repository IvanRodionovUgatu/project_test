class Employee:
    def get_paid(self):
        pass


class Manager(Employee):
    def get_paid(self):
        return 50000


class Worker(Employee):
    def get_paid(self):
        return 30000


m1 = Manager()
w1 = Worker()

print(f'Менеджер получил зарплату: {m1.get_paid()}')
print(f'Работник получил зарплату: {w1.get_paid()}')