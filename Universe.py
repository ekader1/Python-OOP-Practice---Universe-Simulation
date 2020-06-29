from Star import *


class Universe:
    def __init__(self, number_of_stars):

        self.stars = []
        self.number_of_stars = number_of_stars
        #DWARFSTAR
        self.dwarf_counter = 0
        self.total_gaseous_dwarf = 0
        self.total_rocky_dwarf = 0
        self.total_habitable_dwarf = 0
        #MEDIUMSTAR
        self.medium_counter = 0
        self.total_gaseous_medium = 0
        self.total_rocky_medium = 0
        self.total_habitable_medium = 0
        #GIANTSTAR
        self.giant_counter = 0
        self.total_gaseous_giant = 0
        self.total_rocky_giant = 0
        self.total_habitable_giant = 0
        self.lifeFound = 0
        #GENERATE UNIVERSE
        self.generateUniverse()

        self.number_of_planets()

    def generateUniverse(self):
        for i in range(self.number_of_stars):
            self.starGenerationWay = randint(1, 3)
            if self.starGenerationWay == 1:
                self.star = DwarfStar()
                self.stars.append(self.star)
                self.dwarf_counter += 1
            elif self.starGenerationWay == 2:
                self.star = MediumStar()
                self.stars.append(self.star)
                self.medium_counter += 1
            elif self.starGenerationWay == 3:
                self.star = GiantStar()
                self.stars.append(self.star)
                self.giant_counter += 1

    def number_of_planets(self):
        for i in self.stars:
            if isinstance(i, DwarfStar):
                for j in i.planets:
                    if isinstance(j, RockyPlanet):
                        self.total_rocky_dwarf += 1
                    elif isinstance(j, GaseousPlanet):
                        self.total_gaseous_dwarf += 1
                    elif isinstance(j, HabitablePlanet):
                        self.total_habitable_dwarf += 1
                        possibility_of_life = randint(1, 10000)
                        if (possibility_of_life in range(1,9)) and (j.star_distance > 30) and (j.star_distance < 90):
                            j.having_life = True


            elif isinstance(i, MediumStar):
                for j in i.planets:
                    if isinstance(j, RockyPlanet):
                        self.total_rocky_medium += 1
                    elif isinstance(j, GaseousPlanet):
                        self.total_gaseous_medium += 1
                    elif isinstance(j, HabitablePlanet):
                        self.total_habitable_medium += 1
                        possibility_of_life = randint(1, 10000)
                        if (possibility_of_life in range(1, 9)) and (j.star_distance > 40) and (j.star_distance < 140):
                            j.having_life = True
            elif isinstance(i, GiantStar):
                for j in i.planets:
                    if isinstance(j, RockyPlanet):
                        self.total_rocky_giant += 1
                    elif isinstance(j, GaseousPlanet):
                        self.total_gaseous_giant += 1
                    elif isinstance(j, HabitablePlanet):
                        self.total_habitable_giant += 1
                        possibility_of_life = randint(1, 10000)
                        if (possibility_of_life in range(1, 9)) and (j.star_distance > 100) and (j.star_distance < 250):
                            j.having_life = True

    def display_universe(self):
        print("There are", self.number_of_stars, "stars in my universe:")
        print("There are", self.dwarf_counter, "Dwarf Stars with: ")
        print(self.total_gaseous_dwarf, "Gaseous Planets")
        print(self.total_rocky_dwarf, "Rocky Planets")
        print(self.total_habitable_dwarf, "Habitable Planets")
        print("There are", self.medium_counter, "Medium Stars with:")
        print(self.total_gaseous_medium, "Gaseous Planets")
        print(self.total_rocky_medium, "Rocky Planets")
        print(self.total_habitable_medium, "Habitable Planets")
        print("There are", self.giant_counter, "Giant Stars with:")
        print(self.total_gaseous_giant, "Gaseous Planets")
        print(self.total_rocky_giant, "Rocky Planets")
        print(self.total_habitable_giant, "Habitable Planets")












