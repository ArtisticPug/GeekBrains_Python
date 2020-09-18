import itertools


def repeater(repeated_list):  # Повторяет элементы указанного списка Repeats раз
    i = 0
    a = True
    while a == True:
        try:
            repeats = int(input("Укажите число повторений: "))
            while i < repeats:
                for el in repeated_list:
                    print(el, end=" ")
                i += 1
            a = False
        except TypeError:
            print("Нужно ввести число!")
        except ValueError:
            print("Нужно ввести число!")


def counter(to_count_list):  # доваляет в лист элементы с start по 10
    try:
        start = int(input("Введите число от 0 до 10: "))
        for el in itertools.count(start):
            if el > 10:
                break
            to_count_list.append(el)
    except TypeError:
        print("Нужно ввести число!")
    except ValueError:
        print("Нужно ввести число!")


gen_list = []
counter(gen_list)
repeater(gen_list)

# a = True
# while a == True:
#     try:
#         counter(int(input("Введите число от 0 до 10: ")))
#         print(gen_list)
#         a = False
#     except TypeError:
#         print("Нужно ввести число!")
#     except ValueError:
#         print("Нужно ввести число!")

# i = 0
# a = True
# while a == True:
#     try:
#         repeats = int(input("Укажите число повторений: "))
#         while i < repeats:
#             for el in gen_list:
#                 print(el, end=" ")
#             i += 1
#         a = False
#     except TypeError:
#         print("Нужно ввести число!")
#     except ValueError:
#         print("Нужно ввести число!")
