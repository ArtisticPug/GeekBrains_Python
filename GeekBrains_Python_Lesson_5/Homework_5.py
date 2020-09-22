with open("HW_5_Numbers.txt", "w+", encoding="UTF-8") as numbers:
    numbers.writelines((input("Input numbers with space inbetween: ")))
    numbers.seek(0)
    sum = 0
    for line in numbers:
        for el in line.split():
            sum += int(el)
    print(sum)
