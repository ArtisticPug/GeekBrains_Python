with open("New_Text_File.txt", encoding="utf-8") as new_text:
    for ind, line in enumerate(new_text, 1):
        print(f"строка № {ind} -", f"кол-во слов в строке: {len(line.split())}")