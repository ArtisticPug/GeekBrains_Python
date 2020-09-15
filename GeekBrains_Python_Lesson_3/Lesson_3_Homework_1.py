def my_func():
    var_1 = int(input("Введите 1 число: "))
    var_2 = int(input("Введите 2 число: "))
    while var_2 == 0:
        var_2 = int(input("Делить на 0 нельзя!\nВведите 2 число: "))
    return int(var_1 / var_2)
print(my_func())
