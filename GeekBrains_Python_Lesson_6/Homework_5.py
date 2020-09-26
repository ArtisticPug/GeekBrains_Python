class Stationery:
    Title = "Default"

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("\033[3m{}\033[0m".format("Запуск отрисовки Ручки."))


class Pencil(Stationery):
    def draw(self):
        print("\033[4m\033[2m{}\033[0m".format("Запуск отрисовки Карандаша."))


class Handle(Stationery):
    def draw(self):
        print("\033[1m{}\033[0m".format("Запуск отрисовки Маркера."))


default = Stationery()
default.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
