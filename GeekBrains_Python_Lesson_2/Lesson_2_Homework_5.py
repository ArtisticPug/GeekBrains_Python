my_list = [7, 5, 3, 3, 2]
i = 0
print("Рейинг: ")
print(my_list)
while i < 5:
    my_list.append(int(input("Введите новое значение: ")))
    my_list = sorted(my_list)
    my_list.reverse()
    print(my_list)
    i += 1