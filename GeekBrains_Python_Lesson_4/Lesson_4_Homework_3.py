# new_list = [el for el in (list(range(20, 241))) if el % 20 == 0]
# print("=" * 20 + " Кратные 20 " + "=" * 20)
# print(new_list)

new_list2 = [el for el in (list(range(20, 241))) if el % 21 == 0 or el % 20 == 0]
print("=" * 20 + " Кратные 20 или 21 " + "=" * 20)
print(new_list2)
