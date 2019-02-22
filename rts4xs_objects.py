from random import choices
from random import randint
from random import uniform

class Countable: 
    '''Several in-game elements will require tracking real
    time changes in attributes. Countable objects will feed into
    more complex objects and eventually a GUI. 
    '''
    def __init__(self, n = "", e = 0.0):
        self.name = n
        self.element = e

    def getElement(self):
        '''return the value of element'''
        return self.element
    def setElement(self, e):
        self.element = e

    def getName(self):
        return self.name
    def setName(self, n):
        self.name = n
    
    def increment(self, v):
        self.element = self.element + v

class Time(Countable):
    '''in game elements must change according to time consider representing the decimal as a seperate number
    '''
    def __init__(self, n = 'Time', e = 2200.0, p = False):
        self.name = n
        self.element = e
        self.playing = p
    
    

class Resource(Countable):
    '''in game element that increments and can be used to supply and maintain
    ships, buildings, infastructure, research
    '''
    


class Celestial:
    '''in game element characterizing any meaningful object in space. requires the ability to have subelements.
    Attributes:
        celestials: array of objects orbiting around the main celestial object. 
        e.g. if the celestial is a star this would include asteroids and planets and comets
        e.g. if the celestial is a planet this would include any moons that orbit around the planet
        the index of the celestial represents its relative position within the celestial body. if the celestial body is a sun,
        the 0 index would be mercury


    '''
    def __init__(self):
        self.celestials = []
        self.resources = []
        self.buildings = []
        self.ships = []
        self.name = ''
        self.type = ''

    def init_celestials(self):
        pass
    def init_resources(self):
        pass
    
    def getName(self):
        return self.name
    def setName(self, n):
        self.name = n
    def getType(self):
        return self.type
    def setType(self, t):
        self.type = t

    def get_celestials(self):
        return self.celestials
    def set_celestial(self, index, celestial):
        self.celestials[index] = celestial
    def append_celestial(self, celestial):
        self.celestials.append(celestial)
    def get_resources(self):
        return self.resources
    def set_resources(self, index, resource):
        self.resources[index] = resource
    def append_resource(self, resource):
        self.resources.append(resource)
    def get_buildings(self):
        return self.buildings
    def set_building(self, index,  building):
        self.buildings[index] = building
    def append_building(self, building):
        self.buildings.append(building)
    def get_ships(self):
        return self.ships
    def set_ship(self, index, ship):
        self.ships[index] = ship
    def append_ship(self, ship):
        self.ships.append(ship)
    

        

class Planet(Celestial):
    def __init__(self, p, ra, atm, t):
        self.position = p
        self.resource_array = ra
        
        self.atmosphere = atm
        
        self.tiles = t
        self.buildings = None
        self.population = None

    

    



class GasGiant(Planet):
    pass

class TerraPlanet(Planet):
    pass

class Asterioid(Celestial):
    pass

class Comet(Celestial):
    pass


class Star(Celestial):
    '''characterizes a Star, of which there
    may be up to three within a solar system
    '''

    def __init__(self):
        
        '''
        consider including subcategories and determining the rest of
        the stars properties more inline with reality
        atm temperatures will be more inline with main sequence stars
        upon generating solar systems we will handle rare cases like 
        black holes and temperatures / luminosity for giants
        
        '''

        self.category = choices(['O', 'B', 'A', 'F', 'G', 'K', 'M'] \
            ,[.025,.025,.075,.075,.2,.2,.4])
        
        self.temperature = randint(3500,7500)
        
        self.mass = 1.989 * uniform(.3, 1.7) #scaled by  the 10^30kg
        
        self.radius = uniform(.4,1.3)
        
        self.luminosity = uniform(.04, 6)

    #gets and sets

    def getCategory(self):
        return self.category
    def getTemperature(self):
        return self.temperature
    def getMass(self):
        return self.mass
    def getRadius(self):
        return self.radius
    def getLuminosity(self):
        return self.luminosity

    def setCategory(self, c):
        self.category = c
    def setTemperature(self, t):
        self.temperature = t
    def setMass(self, m):
        self.mass = m
    def setRadius(self, r):
        self.radius = r
    def setLuminosity(self, l):
        self.luminosity = l


        

    


    

