class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        a = f"{list(self.rows)}".replace("[[", "[")
        a = f"{a}".replace("]]", "]")
        a = f"{a}".replace("], [", "]\n[")
        return f"{a}".replace(", ", " ")

    def __add__(self, other):
        try:
            c = []
            for el in list(self.rows):
                sum_list = []
                for i in el:
                    sum = i + list(other.rows)[list(self.rows).index(el)][el.index(i)]
                    sum_list.append(sum)
                c.append(sum_list.copy())
                sum_list.clear()
            return Matrix(c)
        except IndexError:
            return "Error! You can only add up matrix of same size!"


a = Matrix([[1, 2, 3, 13], [4, 5, 6, 14], [7, 8, 9, 15], [10, 11, 12, 16]])
b = Matrix([[1, 2, 3, 13], [4, 5, 6, 14], [7, 8, 9, 15], [10, 11, 12, 16]])

print(a), print(), print(b), print(), print(a + b), print(), print(type(a + b))
