from Universe import Universe
from random import randint
from Probe import *


def main():

    my_universe = Universe(2**15)
    my_universe.display_universe()
    my_probe = Probe(my_universe, randint(2**3, 2**64), randint(2**3, 2**64), randint(2**3, 2**64))
    my_probe.search_for_life()

if(__name__ == "__main__"):
    main()
