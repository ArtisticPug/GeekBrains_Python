import ctypes

kernel32 = ctypes.windll.kernel32  # Без этой части, которую с свзял из https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)  # В консоли не отображались цвета
from os import system, name
from time import sleep


def clear():  # Окно Run Python не смог очищать... Однако файл .py запущений с помощью системной консольки интерпретатора отлично очищается
    if name == 'nt':
        _ = system('cls')


class TrafficLight:
    TrafficLight_color = {"Red": ["\033[31m {}\033[0m", 7, "R"], "Yellow": ["\033[33m {}\033[0m", 2, "Y"],
                          "Green": ["\033[32m {}\033[0m", 5, "G"], "Yellow2": ["\033[33m {}\033[0m", 2, "Y"]}  # Не получилось заставить мигать :'( \033[5m или \033[6m не сработали...

    def running(self):
        n = 0
        while n < 2:
            for _ in TrafficLight.TrafficLight_color.keys():
                w = list(TrafficLight.TrafficLight_color.get(_))[0]
                c = list(TrafficLight.TrafficLight_color.get(_))[1]
                i = list(TrafficLight.TrafficLight_color.get(_))[2]
                print((f"{w}").format(f"- - {i} - -\n"
                                      f" - {i} {i} {i} -\n"
                                      f" {i} {i} {i} {i} {i}\n"
                                      f" - {i} {i} {i} -\n"
                                      f" - - {i} - -"))
                sleep(c)
                clear()
            n += 1


a = TrafficLight()
a.running()
