import json
with open("my_json_list.json", "r", encoding="UTF-8") as my_json:
    data = json.load(my_json)
    print(data)

