class Storage:
    storage = []


class Item:
    def __init__(self, producer, name):
        self.producer = producer
        self.name = name

    def move_to(self, where):
        where.append(self)


class Printer(Item):
    def __init__(self, producer, name, color):
        super().__init__(producer, name)
        self.color = color

    def __str__(self):
        a = {f"{self.Class}": [f"{self.producer}", f"{self.name}", f"{self.color}"]}
        return str(a)

    @property
    def Class(self):
        return "Printer"


class Scanner(Item):
    def __init__(self, producer, name, size):
        super().__init__(producer, name)
        self.size = size

    def __str__(self):
        a = {f"{self.Class}": [f"{self.producer}", f"{self.name}", f"{self.size}"]}
        return str(a)

    @property
    def Class(self):
        return "Scanner"


class Xerox(Item):
    def __init__(self, producer, name, wireless):
        super().__init__(producer, name)
        self.wireless = wireless

    def __str__(self):
        a = {f"{self.Class}": [f"{self.producer}", f"{self.name}", f"{self.wireless}"]}
        return str(a)

    @property
    def Class(self):
        return "Xerox"


storage = Storage()
storage = storage.storage
office = Storage()
office = office.storage
factory = Storage()
factory = factory.storage
printer_1 = Printer("Toshiba", "MX-4", "Black")
scanner_1 = Scanner("Siemens", "SC-1", "Small")
xerox_1 = Xerox("LG", "X1", True)
xerox_1.move_to(storage)
print(storage[0])