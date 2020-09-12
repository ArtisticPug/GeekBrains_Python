goods = []
analytics = {}
my_list = []
goods_dict = {"название": 0, "цена": 0, "количество": 0, "eд": 0}

i = 0
n = 1

while i <= 2:
    for el in goods_dict.keys():
        goods_dict[el] = input(f"Введите {el}: ")
    n = str(n)
    tupple_to_add = (n, goods_dict.copy())
    goods.append(tupple_to_add)
    n = int(n)
    n += 1
    i += 1

print("-----" * 10)

for el in goods:
    print(el)

print("-----" * 10)

n = 0
i = 0

while i <= (len(goods[0][1]) - 1):
    b = list(goods[0][1])
    b = b[n]
    for tuple in goods:
        a = list(tuple[1].values())
        my_list.append(a[n])
    add = {b: my_list.copy()}
    my_list.clear()
    analytics.update(add)
    n += 1
    i += 1

for el in analytics:
    print(f"{el} : {analytics.get(el)}")

print("-----" * 10)
