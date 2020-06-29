Design Patterns

* Universe Class Requirements:
    The __init__ method takes the number of stars to create
    Contain a print universe method that prints required data
* Star Class Requirements:
    Star Base Class with unique x, y, z coordinates in the range 2**8..2**64
    Star SubClasses: DwarfStar, GiantStar, MediumStar
    Each Star subtype has attributes: chances of life, number of planets (as a range), goldilocks zone, recharge amount
    Stars generate and save a list of planets using the above attributes
    Star Coordinates are verifiably unique
    Instance variables follow python conventions for private data
* Planet Class Requirements:
   Planet base class that contains distance from star
   Planet SubClasses: RockyPlanet, GaseousPlanet, HabitablePlanet
   Each Planet is marked with having or not having intelligent life based on star attributes and distance from star
   Each planet has a unique identifier as described.
* Probe Class Requirements:
    Keeps track of the requested information
    Unique algorithm to determine which Star should be visited next
    Has a fuel attribute that depletes during the search algorithm, and recharges using the recharge amount for each star
    A print method that prints the probe’s findings.


## Part 1

### Part A - The Stars

You should first create a Universe class as a container class for all your stars, with a method to generate your universe. The stars should derive from a base star class, and fall into one of 3 categories. Each Star type will have attributes that will affect its likelihood of intelligent life:

* DwarfStar
   * Chances of life: 0.0006
   * Range of planets: 8-15
   * Goldilocks Zone: 30-90
   * Recharge: 2**20
* GiantStar
   * Chances of life: 0.0005
   * Range of planets: 5-10
   * Goldilocks Zone: 100-250
   * Recharge: 2**30
* MediumStar
   * Chances of life: 0.0009
   * Range of planets: 2-9
   * Goldilocks Zone: 60-140
   * Recharge: 2**25


Each star will have an x,y,z coordinate to give it a location in space. No two stars should have the same x, y, z coordinates. You will need to use these coordinates to navigate from star to star, so the coordinates must be readable but should not be writable, using python private variable conventions. You should randomly generate these x,y,z coordinates, each in the range of (2^3..2^64)-1.  

Each star should also have a recharge amount to be used by the probe to refuel. A larger star should have a higher recharge amount. For example, I use 2^20, 2^25, 2^30 for the Dwarf, Medium, and Giant Stars respectively. You can adjust these numbers to suit your program, but it must be *possible* to run out of fuel.

Lastly, each star will randomly generate a list of planets (more information on planets below). It should have num planets, where num is in the range of planets given above (inclusive). When you generate the planets, you will need to also randomly assign the planet’s distance from the star in millions of miles. Multiple planets can have the same distance from a star.

### Part B - Planets


Each star will have multiple planets, each with 3 different types:

* RockyPlanet
* GaseousPlanet
* HabitablePlanet

You should randomly assign planet types as they are created, and each Planet should derive from a base Planet class. The Planet base class should contain the planet’s distance from the star in millions of miles.

For example, One star, which is a Giant, may have 6 planets, 2 Rocky, 3 Gaseous, and 1 Habitable. Another Giant Star might have 8 planets, all of which are Gaseous.

Each planet should also have a unique id, preceded by a letter identifying what kind of planet it is, ‘r’ for Rocky, ‘g’ for Gaseous, and ‘h’ for Habitable.


### Part C - Life

We will be using the Star’s chances of life instance variable to mark if a planet has intelligent life. Even if the planet is marked as possible for intelligent life, it then must be within the so-called goldilocks zone for its star and must be a HabitablePlanet type.

If all of these conditions are met, you should mark the planet as having intelligent life. Otherwise, mark it as without life.

Once you have your universe set up, you should add a method to your Universe class that prints the number of stars of each type and how many planets of each type correspond to each star. (See below for sample output)

## Part 2 - The Search

### Part A - Searching for Life
Once you have generated your universe with stars, planets, and (possibly) life, it’s time to search for life. To do so you will need a ‘probe’ object that will search star to star, using an algorithm of your choosing to select which star to go to next. In this README you must explain your search algorithm, and defend why you chose it.


As you visit each star you will use fuel. Your probe will have an initial fuel amount, and can recharge at each star. The recharge amount depends on the type of star you are visiting. After recharging, your probe will check the Star’s planets, and should mark that star as visited so you don’t revisit already explored stars.  Your search ends when your probe finds a planet with intelligent life. In order for your probe to deliver the information, it must have enough fuel to return to its starting point, which means you have to keep track of the probe’s starting coordinates.

You will need to keep track of some data as you explore your simulated universe.

* The probe's starting coordinates
* How many Stars you have visited
* How many Planets you have explored
* The total distance you have traveled before finding intelligent life
   * You can use the [3 dimensional distance formula](https://www.varsitytutors.com/hotmath/hotmath_help/topics/distance-formula-in-3d) to determine the distance between stars.  

When you finally find life and successfully return to the origin, the probe should print the above information and the unique ID of the planet that contained life.

If no life was found or the probe runs out of fuel, print the above information and a message noting this.

### Part B - Requirements

The following are the basic requirements for your program:

#### Universe Class Requirements:

* The initialize method takes the number of stars to create
    * For testing, you should start out with around 2**10 or less. After you get it working, see how large you can go and still run within a reasonable amount of time.
* Should contain a print universe method that prints:
    * The number of stars in the universe
    * The number of each type of star
    * The number of each type of planet around each type of star
        * See below for example

#### Star Class Requirements:

* Star Base Class with unique x, y, z coordinates in the range 2**3..2**64
* Star SubClasses: DwarfStar, GiantStar, MediumStar
* Each Star subtype has attributes:
    * chances of life
    * number of planets (as a range)
    * goldilocks zone
    * Stars should generate and save a list of planets using the above attributes

#### Planet Class Requirements:

* Planet base class that contains distance from star ranging from 1-300 (in 10 millions of miles)
* Planet SubClasses: RockyPlanet, GaseousPlanet, HabitablePlanet
* Each Planet is marked with having or not having intelligent life
* Each planet should have a unique identifier.
    * implementation is up to you as long as it is guaranteed to be unique and is prefixed with the appropriate letter (i.e. ‘r’, ‘g’, ‘h’)

###Probe Class Requirements:

* Keeps track of the following information
    * starting coordinates
    * id of planet discovered to have intelligent life
    * total distance traveled
    * number of stars visited
    * number of planets explored
* An algorithm to determine which Star you should visit next
* A print method that prints the probe’s findings.


### Additional Requirements

* You must use composition for all HAS-A relationships.
    * For example, the planet class should not inherit from the Star class. You must have a compositional relationship between the Star and the Planet.         
* Each base class must go into a separate file. Subclasses *may* go in the same file as their base class.
* The main driver code should also be in a separate file.
* You should not have any global variables

## Sample Output:

This was run with 2**10 stars:

```
Total number of stars in my universe: 1025
There are 380 Giant Stars with:
        1056 Gaseous Planets
        1092 Rocky Planets
        1082 Habitable Planets
        0 Planets with Intelligent Life

There are 303 Dwarf Stars with:
        1275 Gaseous Planets
        1219 Rocky Planets
        1277 Habitable Planets
        0 Planets with Intelligent Life

There are 342 Medium Stars with:
        715 Gaseous Planets
        747 Rocky Planets
        807 Habitable Planets
        1 Planets with Intelligent Life

==========

Your origin was (4576, 76584476, 46508759)
Traveled 1.6731455226093466e+20 miles
        You have 5.870783888950368e+3 fuel remaining
        Visited 131 stars
        Explored 1223 planets
Found life on planet h8657
```

