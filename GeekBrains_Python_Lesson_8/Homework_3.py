class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
i = 0

while True:
    a = input("input number or 'q' to finish: ")
    try:
        if a == "q":
            break
        elif a.isdigit() == True:
            my_list.append(a)
        else:
            raise NotNumber("Only numbers!")
    except NotNumber as err:
        print(err)

print(my_list)
