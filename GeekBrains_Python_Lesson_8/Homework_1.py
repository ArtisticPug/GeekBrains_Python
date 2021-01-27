class Date:
    """Принимает дату в формате ДД-ММ-ГГГГ"""

    def __init__(self, date):
        self.date = date

    @classmethod
    def First(self, date):
        for el in date.split("-"):
            print(int(el), end=" ")

    @staticmethod
    def Second(date):
        if 1 <= int(date.split("-")[0]) <= 30:
            print(date.split("-")[0])
            print("День указан верно!")
        else:
            print("День указан не верно!")

        if 1 <= int(date.split("-")[1]) <= 12:
            print(date.split("-")[1])
            print("Месяц указан верно!")
        else:
            print("Месяц указан не верно!")

        if 1 <= int(date.split("-")[2]) <= 9999:
            print(date.split("-")[2])
            print("Год указан верно!")
        else:
            print("Год указан не верно!")


date = Date("02-10-2020")
print(date.date)

date.First("02-10-2020"), print()
Date.Second("30-10-2020")
