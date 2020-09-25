class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self.wage = w
        self.bonus = b
        self._income = {"wage": f"{self.wage}", "bonus": f"{self.bonus}"}


class Position(Worker):
    def get_full_name(self):
        print(f"Name: {self.name}, {self.surname}")

    def get_total_income(self):
        print(f"Total income: {self.wage + self.bonus}")


admin = Position("Andrei", "Kolobkov", "sisadmin", 50000, 25000)
admin.get_full_name(), admin.get_total_income()

manager = Position("Vitaliy", "Sokolov", "manager", 40000, 15000)
manager.get_full_name(), manager.get_total_income()
