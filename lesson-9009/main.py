import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, coords=None):
        if coords is None:
            self._coords = [0,0,0]
        else:
            self._coords = coords
        self.speed = speed

    def move(self, dx, dy, dz):
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed
        if self._coords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {int(self._coords[0])}, Y: {int(self._coords[1])}, Z: {int(self._coords[2])}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random.choice
        print(f"Here are(is) {random.choice(range(1,4+1))} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.speed = self.speed * 0.5
        self.move(0, 0, -abs(dz))
        self.speed = self.speed * 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

if __name__ == "__main__":
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