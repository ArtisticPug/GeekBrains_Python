class Road:
    _coif = 25 * 5

    def __init__(self, len, wid):
        self._length = len
        self._width = wid

    def calculate(self):
        result = self._length * self._width * self._coif / 1000
        print(f"{int(result)} т")


a = Road(20, 5000)
a.calculate()
