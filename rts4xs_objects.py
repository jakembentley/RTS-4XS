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

class Resource(Countable):
    '''in game element that increments and can be used to supply and maintain
    ships, buildings, infastructure, research
    '''
    pass

class Celestial:
    '''in game element characterizing any meaningful object in orbit in a solar
    system. Typically exploited for events or resources. anywhere from a a gas giant to a comet
    '''

    pass

class Planet(Celestial):
    pass

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


        

    


    

