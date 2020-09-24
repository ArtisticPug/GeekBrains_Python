import json

my_list = [{}, {}]
with open("HW_7.txt", "r+", encoding="UTF-8") as firms:
    # print("=" * 10 + " Все фирмы " + "=" * 10 + "\n")
    for line in firms:
        # print(f"{line.split()[0]}: {(int(line.split()[2]) - int(line.split()[3]))}")
        my_list[0].update({(line.split()[0]): (int(line.split()[2]) - int(line.split()[3]))})
    firms.seek(0)
    # print("\n" + "="*10 + " Прибыльные фирмы " + "="*10 + "\n")
    summ = 0
    count = 0
    for line in firms:
        if (int(line.split()[2]) - int(line.split()[3])) > 0:
            # print(f"{line.split()[0]}: {(int(line.split()[2]) - int(line.split()[3]))}")
            summ += (int(line.split()[2]) - int(line.split()[3]))
            count += 1
    # print("\n" + "=" * 10 + " Средняя прибыль фирм " + "=" * 10 + "\n")
    # print(summ / count)
    my_list[1].update({"average profit": (summ / count)})
    # print(my_list)
with open("my_json_list.json", "w", encoding="UTF-8") as my_json:
    json.dump(my_list, my_json)