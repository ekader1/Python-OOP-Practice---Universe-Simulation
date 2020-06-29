from Universe import *
import math

class Probe:
    def __init__(self, universe, starting_point_x, starting_point_y, starting_point_z,  starting_fuel=2**70, distance_traveled=0, visited_stars=None, explored_planets=None, life_found=False):
        if visited_stars is None:
            visited_stars = []
        if explored_planets is None:
            explored_planets = []

        self.universe = universe
        self.starting_fuel = starting_fuel
        self.starting_point_x = starting_point_x
        self.starting_point_y = starting_point_y
        self.starting_point_z = starting_point_z
        self.distance_traveled = distance_traveled
        self.visited_stars = visited_stars
        self.explored_planets = explored_planets
        self.life_found = life_found

    def distance_between(self, first_point_x, second_point_x, first_point_y, second_point_y, first_point_z, second_point_z):
        distance_between2 = math.sqrt((first_point_x - second_point_x)**2 + (first_point_y - second_point_y)**2 + (first_point_z - second_point_z)**2)
        return distance_between2

    def search_for_life(self):

        for i in self.universe.stars:
            if self.starting_fuel == 0:
                print("Ups. Out of fuel, you are in real trouble")
            self.visited_stars.append(i)
            distance_2_point = self.distance_between(self.starting_point_x, i.x, self.starting_point_y, i.y, self.starting_point_z, i.z)
            self.distance_traveled = self.distance_traveled + distance_2_point
            self.starting_fuel = self.starting_fuel - distance_2_point
            self.starting_fuel = self.starting_fuel + i.recharge

            for j in i.planets:
                if self.starting_fuel == 0:
                    print("Ups. Out of fuel, you are in real trouble")
                self.explored_planets.append(j)
                self.starting_fuel = self.starting_fuel - 2 * j.star_distance
                self.distance_traveled = self.distance_traveled + 2 * j.star_distance

                if j.having_life == True:
                    self.life_found = True
                    print("Your origin was:", self.starting_point_x, " ", self.starting_point_y, " ", self.starting_point_z)
                    print("Traveled", self.starting_fuel, "miles")
                    print("Life has found on ", j.planet_id, ",", j.star_distance, "miles away from it's star")
                    print(len(self.visited_stars), "stars visited")
                    print(len(self.explored_planets), "planets explored")
                    return



        if self.life_found == False:
            print("We are alone in this universe, no life detected")
            print("Your origin was:", self.starting_point_x, " ", self.starting_point_y, " ", self.starting_point_z)
            print("Traveled", self.distance_traveled, "miles")
            print(len(self.visited_stars), "stars visited")
            print(len(self.explored_planets), "planets explored")














                








