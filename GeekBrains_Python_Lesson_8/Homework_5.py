class ComplexNum:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __str__(self):
        return str(complex(self.n1, self.n2))

    def __add__(self, other):
        result = complex(self.n1, self.n2) + complex(other.n1, other.n2)
        return str(complex(result))

    def __mul__(self, other):
        result = complex(self.n1, self.n2) * complex(other.n1, other.n2)
        return str(complex(result))


a = ComplexNum(5, 6)
b = ComplexNum(3, 8)
print(a + b)
print(a * b)
