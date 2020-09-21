from sys import argv

script_name, pay, hour, bonus = argv
(int(pay) * int(hour)) + int(bonus)
print(f"Итого заработная плата: {(int(pay) * int(hour))} + {int(bonus)} = {(int(pay) * int(hour)) + int(bonus)}")
