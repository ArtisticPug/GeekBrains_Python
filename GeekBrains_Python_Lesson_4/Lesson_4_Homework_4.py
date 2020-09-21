import random

initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]  # result = [23, 1, 3, 10, 4, 11]
new_list = [el for el in initial_list if initial_list.count(el) <= 1]
print("=" * 20 + " Исходный список " + "=" * 20)
print(initial_list)
print(new_list)

generatedlist = []
i = 0
while i < 10:
    generatedlist.append(int(format(random.random() * 100, '.0f')))
    i += 1
new_list2 = [el for el in generatedlist if generatedlist.count(el) <= 1]
print("=" * 20 + " Случайный список " + "=" * 20)
print(generatedlist)
print(new_list2)
