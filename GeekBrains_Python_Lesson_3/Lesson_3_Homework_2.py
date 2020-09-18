def my_func(**kwargs):
    a = {"Имя": "", "Фамилия": "", "Год рождения": "", "Город проживания": "", "Email": "", "Номер телефона": ""}
    for el in a:
        a.update({el: (input(f"Введите {el}: "))})
    for el in a:
        print(f"{el}: {a.get(el)}, ", end="")

def second_func(name, lastname, year, city, email, phone):
    print(f"Имя: {name}, Фамилия: {lastname}, Год рождения: {year}, Город проживания: {city}, Email: {email}, Номер телефона: {phone}")

second_func((input("Укажите ваше имя: ")), (input("Укажите вашу фамилию: ")), (input("Укажите ваш год рождения: ")), (input("Укажите ваш город проживания: ")), (input("Укажите ваш Email: ")), (input("Укажите ваш номер телефона: ")))
