with open("HW_3_Workers.txt", "r", encoding="UTF-8") as  workers:
    print("Сотрудники, чей оклад ниже 20тыс рублей: ", end="")
    for line in workers:
        if float(line.split()[1]) >= 20000:
            print(line.split()[0], end=" ")
    sum = 0
    num = 0
    workers.seek(0)
    for line in workers:
        sum += float(line.split()[1])
        num += 1
    print("\nСредний доход всех сотрудников фирмы: ", end="")
    print(f"{sum / num}p")
