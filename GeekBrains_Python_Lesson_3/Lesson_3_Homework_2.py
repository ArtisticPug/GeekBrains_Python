def my_func(**kwargs):
    a = {"Имя": "", "Фамилия": "", "Год рождения": "", "Город проживания": "", "Email": "", "Номер телефона": ""}
    for el in a:
        a.update({el: (input(f"Введите {el}: "))})
    for el in a:
        print(f"{el}: {a.get(el)}, ", end="")


my_func()
