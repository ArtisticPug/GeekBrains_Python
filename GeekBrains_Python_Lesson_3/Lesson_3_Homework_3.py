def my_func():
    a = []
    i = 0
    while i < 3:
        while True:
            try:
                b = int(input(f"Ведите {i + 1} число: "))
                if type(b) == int:
                    break
            except ValueError:
                print("Нужно ввести число.")
        i += 1
        a.append(b)
    a.remove(min(a))
    print(a)

def second_func(var_1, var_2, var_3):
    a = []
    a.append(var_1)
    a.append(var_2)
    a.append(var_3)
    a.remove(min(a))
    print(a)

second_func(4, 8, 5)
