new_text = open("New_Text_File.txt", "a", encoding="utf-8")
print("Вводите текст построчно. Чтобы закончить оставьте строку пустой и нажмите Enter.\n")
while True:
    i = input()
    if len(i) == 0:
        break
    new_text.write(f"{i}\n")
new_text.close()
