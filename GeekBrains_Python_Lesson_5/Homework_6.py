# def cut(line, index):
#     return ((line.split())[index][:((len(list(line.split())[index]) - (int(index) + 2)) if (len(list(line.split())[index])) > 1 else len(list(line.split())[index])):])
def convert(line, index):
    a = ((line.split())[index][:((len(list(line.split())[index]) - (int(index) + 2)) if (len(list(line.split())[index])) > 1 else len(list(line.split())[index])):])
    if len(a) > 1:
        return int(a)
    else:
        return int(0)

with open("HW_6.txt", "r+", encoding="UTF-8") as lesson:
    lessons = {}
    for line in lesson:
        # print(cut(line, 1), end=" ")
        # print(cut(line, 2), end=" ")
        # print(cut(line, 3), end=" ")
        # print(f" Суммарное кл-во часов: {convert(line, 1) + convert(line, 2) + convert(line, 3)}")
        lessons.update({line.split()[0]: (convert(line, 1) + convert(line, 2) + convert(line, 3))})
    print(lessons)
        # print((line.split())[1][:((len(list(line.split())[1]) - 3) if (len(list(line.split())[1]))>1 else len(list(line.split())[1])):], end=" ") # убираем буквы (л) для преобразования в Int
        # print((line.split())[2][:((len(list(line.split())[2]) - 4) if (len(list(line.split())[2]))>1 else len(list(line.split())[2])):], end=" ") # убираем буквы (пр) для преобразования в Int
        # print((line.split())[3][:((len(list(line.split())[3]) - 5) if (len(list(line.split())[3]))>1 else len(list(line.split())[3])):]) # убираем буквы (лаб) для преобразования в Int
