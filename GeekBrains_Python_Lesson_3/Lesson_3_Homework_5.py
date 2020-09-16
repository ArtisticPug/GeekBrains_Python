def my_func():
    repeat = True
    final_summ = 0
    while repeat == True:
        try:
            b = (input("Ведите числа через пробел, чтобы закончить введите букву q: ")).split()
            el_sum = 0
            for el in b:
                if el == "q":
                    repeat = False
                    break
                else:
                    el_sum = el_sum + int(el)
                    final_summ = final_summ + int(el)
            print(f"Сумма указанных элементов: {el_sum}\nИтоговая сумма: {final_summ}")
        except ValueError:
            print("Нужно указать либо число, либо q для прекращения программы!")
my_func()