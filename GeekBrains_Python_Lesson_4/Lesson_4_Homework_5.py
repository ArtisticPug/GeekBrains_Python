import functools


def my_func(prev_el, el):
    return prev_el * el


gen_list = [el for el in list(range(100, 1001)) if el % 2 == 0]
print(functools.reduce(my_func, gen_list))

sum = 1
i = 0
while i < len(gen_list):
    sum = sum * gen_list[i]
    i += 1
print(sum)
if sum == functools.reduce(my_func, gen_list):
    print(True)  # Если умножение было произведено верно
else:
    print(False)  # Если умножение было произведено не верно
