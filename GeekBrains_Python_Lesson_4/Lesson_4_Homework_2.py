import random

initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
generatedlist = []

# print(format(random.random() * 100, '.0f'))
i = 0
while i < 10:
    generatedlist.append(int(format(random.random() * 100, '.0f')))
    i += 1

# for el in generatedlist[1::]:
#     if el > generatedlist[generatedlist.index(el) - 1]:
#         print(el)

new_list = [el for el in initial_list[1::] if initial_list.index(el)==0 or el > initial_list[initial_list.index(el) - 1]]
new_list2 = [el for el in generatedlist[1::] if generatedlist.index(el)==0 or el > generatedlist[generatedlist.index(el) - 1]]

print("=" * 20 + " Исходный список " + "=" * 20)
print(initial_list)
print(new_list)
print("=" * 20 + " Случайный список " + "=" * 20)
print(generatedlist)
print(new_list2)

