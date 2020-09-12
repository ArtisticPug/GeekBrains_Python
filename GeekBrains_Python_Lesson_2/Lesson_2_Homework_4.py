words = input("Введите несколько слов через пробел: ")
words.split()
for number, el in enumerate(words.split(), 1):
    print(number, el[0:10])
