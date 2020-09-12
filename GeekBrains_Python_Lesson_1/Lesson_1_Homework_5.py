profit = int(input('Введите размер выручки: '))
deficit = int(input('Введите размер издержек: '))
money = profit - deficit
money = float('{:.2f}'.format(money))
print(money)
if profit > deficit:
    print('Фирма прибыльна')
    rent = profit / deficit
    rent = float('{:.2f}'.format(rent))
    print(f'Рентабельность предприятия равна: {rent}')
    employees = int(input('Укажите количество сотрудников фирмы: '))
    per_employee = (profit - deficit) / employees
    per_employee = float('{:.2f}'.format(per_employee))
    print(f'На каждого сотрудника приходится: {per_employee}р прибыли')
else:
    print('Фирма убыточна')