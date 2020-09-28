import ctypes

kernel32 = ctypes.windll.kernel32  # Без этой части, которую с свзял из https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)  # В консоли не отображались цвета
from os import system, name
from time import sleep


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

sleep(5)
