from random import randint


class Animal:
    live: bool = True
    sound: str = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, cords=None):
        self._cords = [0, 0, 0] if cords is None else cords
        self.speed = speed

    def move(self, dx, dy, dz):
        x, y, z = self.speed * dx, self.speed * dy, self.speed * dz
        self._cords[1] += y
        self._cords[0] += x
        if self._cords[2] + z < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0
        else:
            self._cords[2] += z

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    def __init__(self, speed):
        self.beak: bool = True
        super().__init__(speed)

    @staticmethod
    def lay_eggs():
        print(f'Here are(is) {randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    # def dive_in(self, dz):
    # """ В воздухе скорость обычная
    #     В воде скорость погружения в два раза меньше
    # """
    #     if self._cords[2] <= 0:
    #         self._cords[2] -= int(self.speed / 2) * abs(dz)
    #     else:
    #         self._cords[2] -= self.speed * abs(dz)
    #         if self._cords[2] < 0:
    #             self._cords[2] = int(self._cords[2] / 2)

    def dive_in(self, dz):
        """ Скорость погружения всегда в два раза меньше
            Ниже уровня воды не может опуститься
        """
        self._cords[2] -= int(self.speed / 2) * abs(dz)
        if self._cords[2] < 0:
            self._cords[2] = 0


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


if __name__ == '__main__':
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()