class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num <= 0:
            return ("You cannot substract cell bigger than the original!")
        else:
            return Cell(self.num - other.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        return Cell(round(self.num // other.num))

    def __str__(self):
        return f"{self.num}"

    def make_order(self, rows):
        for el in range(1, self.num+1):
            if range(1, self.num + 1)[::].index(el) == 0:
                print("*", end=" ")
            elif range(1, self.num+1)[::].index(el) % rows == 0:
                print("\n*", end=" ")
            else:
                print("*", end=" ")


cell_1 = Cell(20)
cell_2 = Cell(8)

print(cell_1 + cell_2)
print(cell_1 - cell_2), print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 // cell_2), print()
cell_1.make_order(4)


