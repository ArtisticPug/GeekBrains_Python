eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def int_func(var):
    num = 0
    for el in list(var):
        a = eng.count(el)
        if a == 0:
            # (print("Ошибка! Необходимо указать слово из латинских букв!"))
            # return var
            # Не смог решить что выводить в случае если указано слово содержащее не латинские символы
            return "*non_latin_word*"
            break
        if a > 0:
            num+=1
    if num == len(list(var)):
        return var.title()


def second_func():
    words = input("Введите несколько слов на латинском через пробел: ")
    for el in words.split():
        print(int_func(el), end=" ")


print(int_func("house"))
second_func()