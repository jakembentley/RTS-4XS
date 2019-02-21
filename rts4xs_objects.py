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

    def increment(self, v):
        self.element = self.element + v

class Star:
    '''characterizes a Star, of which there
    may be up to three within a solar system
    '''

    def __init__(self):
        
        #the stars properties more inline with reality
        #atm temperatures will be more inline with main sequence stars
        #upon generating solar systems we will handle rare cases like 
        #black holes and temperatures / luminosity for giants
        
        self.category = choices(['O', 'B', 'A', 'F', 'G', 'K', 'M', '_'] \
            ,[.025,.025,.05,.05,.2,.2,.4,.05])
        
        #consider including subcategories and determining the rest of
       
        self.temperature = randint(3500,7500)
        self.mass = 1.989 * uniform(.3, 1.7) #represents mass to the 10^30kg
        self.radius = uniform(.4,1.3)
        self.luminosity = uniform(.04, 6)


    


    

