from random import randint
class Planet:
    def __init__(self, star_distance, planet_id, having_life):
        self.star_distance = star_distance
        self.planet_id = planet_id
        self.having_life = having_life


class RockyPlanet(Planet):
    def __init__(self):
        super().__init__(star_distance = randint(1, 300), planet_id = "r" + str(randint(1,5000)), having_life=False)

class GaseousPlanet(Planet):
    def __init__(self):
        super().__init__(star_distance = randint(1, 300), planet_id = "g" + str(randint(1,5000)), having_life=False)

class HabitablePlanet(Planet):
    def __init__(self):
        super().__init__(star_distance = randint(1, 300), planet_id = "h" + str(randint(1,5000)),having_life=False)




