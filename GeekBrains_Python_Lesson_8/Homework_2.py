class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        a = (int(input("Введите 1 число: ")))
        b = (int(input("Введите 2 число: ")))
        if b == 0:
            raise OwnError("Делить на ноль нельзя!")
    except OwnError as err:
        print(err)
    else:
        print(a / b)
        break
