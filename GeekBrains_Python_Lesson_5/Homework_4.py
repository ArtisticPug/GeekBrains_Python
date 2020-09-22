from googletrans import Translator  # Установил с помощью pip install googletrans

translator = Translator()
# result = translator.translate('two', src='en', dest='ru')
# print(result.text)
new_words = open("HW_4_new.txt", "w", encoding="utf-8")
with open("HW_4.txt", "r+", encoding="UTF-8") as words:
    for line in words:
        result = translator.translate((line.split())[0], src='en', dest='ru')
        new_words.writelines(f"{result.text} — {(line.split())[2]}\n")
new_words.close()
