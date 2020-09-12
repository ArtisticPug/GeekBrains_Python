seasons = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
month = int(input("Введите номер месяца (от 1 до 12): "))
while (month < 1 or month > 12):
    month = int(input("Введите номер месяца (от 1 до 12): "))
for el in seasons:
    el.count(month)
    if el.count(month) > 0:
        if seasons.index(el) == 0:
            print("Вы указали зимный месяц.")
        elif seasons.index(el) == 1:
            print("Вы указали весенний месяц.")
        elif seasons.index(el) == 2:
            print("Вы указали летний месяц.")
        elif seasons.index(el) == 3:
            print("Вы указали осенний месяц.")
        break