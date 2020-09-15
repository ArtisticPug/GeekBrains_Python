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

my_func()
