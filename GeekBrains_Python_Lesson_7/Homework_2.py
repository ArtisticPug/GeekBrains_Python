from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, par):
        self.par = par

    @abstractmethod
    def use(self):
        pass

    def __add__(self, other):
        return round(self.use + other.use, 2)

    def __str__(self):
        return f"{self.use}"


class Coat(Clothing):
    @property
    def use(self):
        return round(self.par / 6.5 + 0.5, 2)


class Suit(Clothing):
    @property
    def use(self):
        return round(2 * self.par + 0.3, 2)

coat_1 = Coat(15)
suit_1 = Suit(10)
coat_2 = Coat(20)

print(type(coat_1))
print(type(coat_1.use))
print((coat_1 + suit_1) * 5)
print(coat_1 + suit_1 + coat_2)