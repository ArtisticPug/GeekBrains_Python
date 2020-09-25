from time import sleep


class Car:
    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = False

    def go(self):
        print(f"Car {self.name} starts moving")
        sleep(1)

    def stop(self):
        print(f"Car {self.name} stops moving\n")
        sleep(1)

    def turn(self, direction):
        directions = ["left", "right"]
        if directions.count(str(direction).lower()) == 1:
            print(f"Car {self.name} turns {direction}")
        else:
            print(f"Car {self.name} decides to ignore command, because it can only turn left or right")
        sleep(1)

    def show_speed(self):
        print(f"Car {self.name} moves with speed of {self.speed} kmp/h")


class TownCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            print("\033[31m{}\033[0m".format(
                "Warning! ") + f"Car {self.name} moves over the speed limit of 60 kmp/h with speed of {self.speed} kmp/h!")
        else:
            print(f"Car {self.name} moves with speed of {self.speed} kmp/h")


class SportCar(Car):
    is_police = False


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            print("\033[31m{}\033[0m".format(
                "Warning! ") + f"Car {self.name} moves over the speed limit of 40 kmp/h with speed of {self.speed} kmp/h!")
        else:
            print(f"Car {self.name} moves with speed of {self.speed} kmp/h")


class PoliceCar(Car):
    is_police = True


lada = TownCar(80, "Green", "Lada")
print(lada.speed), print(lada.name), print(lada.is_police), print(lada.color), print(), sleep(1)
lada.go(), lada.show_speed(), lada.turn("left"), lada.turn("right"), lada.turn("upside"), lada.stop()

ford = WorkCar(45, "Green", "Ford")
ford.go(), ford.show_speed(), ford.turn("Left"), ford.turn("Right"), ford.stop()

mitsubishi = PoliceCar(65, "Green", "Mitsubishi")
mitsubishi.go(), mitsubishi.show_speed(), mitsubishi.turn("left"), mitsubishi.stop()

subaru = SportCar(120, "Green", "Subaru")
subaru.go(), subaru.show_speed(), subaru.turn("left"), subaru.turn("right"), subaru.stop()
