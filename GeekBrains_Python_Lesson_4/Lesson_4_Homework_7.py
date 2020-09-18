import itertools


def recursive_fact(a):
    if a == 0:
        return 1
    else:
        return recursive_fact(a - 1) * a


# def fact(n):
#     a = []
#     b = []
#     for el in itertools.count(0):
#         if el > n:
#             break
#         a.append(el)
#     for el in a:
#         b.append(recursive_fact(el))
#     print(a)
#     print(b)
#
#
# fact(4)

def fact(n):
    for el in range(1, (n + 1)):
        yield recursive_fact(el)


a = 1
for el in fact(6):
    print(f"{a}! = {el};", end=" ")
    a += 1
