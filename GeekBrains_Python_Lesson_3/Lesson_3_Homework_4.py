def my_func(x, y):
    return 1 / x ** abs(y)


def my_secondfunc(x, y):
    i = 1
    b = x
    while i < abs(y):
        b = b * x
        i += 1
    return 1 / b

print(my_func(2, -4))
print(my_secondfunc(2, -4))
