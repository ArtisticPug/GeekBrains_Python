a = int(input('Результат спортсмена в первый день(км): '))
b = int(input('Укажите целевой результат(км): '))
i = 1
while True:
    a = a * 1.1
    i = i +1
    if a >= b:
        break
print(f'На {i}-й день спортсмен достиг результата - не менее {b} км.')