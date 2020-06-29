from Planet import *
from random import randint

class Star:
    def __init__(self, x, y, z, chances_of_life, range_of_planets, goldilocks_zone, recharge, planets=None):
        if planets is None:
            planets = []
        self.x = x
        self.y = y
        self.z = z
        self.planets = planets
        self.chances_of_life = chances_of_life
        self.range_of_planets = range_of_planets
        self.goldilocks_zone = goldilocks_zone
        self.recharge = recharge
        self.generatePlanets()

    def generatePlanets(self):
        for i in range(self.range_of_planets):
            planet_generation_way = randint(1,3)

            if planet_generation_way == 1:
                self.planet = RockyPlanet()
                self.planets.append(self.planet)

            elif planet_generation_way == 2:
                self.planet = GaseousPlanet()
                self.planets.append(self.planet)

            elif planet_generation_way == 3:
                self.planet = HabitablePlanet()
                self.planets.append(self.planet)



class DwarfStar(Star):
    def __init__(self):
        super().__init__(x=randint(2**3, 2**64), y=randint(2**3, 2**64), z=randint(2**3, 2**64),
                             chances_of_life=0.0006, range_of_planets = randint(8, 15), goldilocks_zone = randint(30, 90),
                             recharge = 2 ** 20, planets=None)


class GiantStar(Star):
    def __init__(self):
        super().__init__(x=randint(2 ** 3, 2 ** 64), y=randint(2 ** 3, 2 ** 64), z=randint(2 ** 3, 2 ** 64),
                             chances_of_life=0.0005, range_of_planets=randint(5, 10), goldilocks_zone=randint(100, 250),
                             recharge=2 ** 30,  planets=None)


class MediumStar(Star):
    def __init__(self):
        super().__init__(x=randint(2 ** 3, 2 ** 64), y=randint(2 ** 3, 2 ** 64), z=randint(2 ** 3, 2 ** 64),
                             chances_of_life=0.0009, range_of_planets=randint(2, 9), goldilocks_zone=randint(40, 140),
                             recharge=2 ** 25,  planets=None)


