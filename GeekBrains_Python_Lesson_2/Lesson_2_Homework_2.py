main_input = input("Введите значения через пробел: ")
main_list = list(main_input.split(" "))
print(main_list)
for el in main_list[1::2]:
    main_list.insert((main_list.index(el) - 1), el)
    main_list.pop((main_list.index(el) + 2))
print(main_list)