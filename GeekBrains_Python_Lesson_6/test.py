import colorama
from colorama import Fore, Back, Style
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
import time

colorama.init()
print(Fore.RED + 'Красный текст')
print(Back.BLUE + 'Синий фон')
print(Style.RESET_ALL)
print('Снова обычный текст')

time.sleep(5)
