from random import choices
from random import randint
from random import uniform


class Celestial:
    '''
    @attr celestials: an array of celestials whose index indicates proximity to main celestial. length is determined on construction. dependent on subclass
    @attr resources: a dict of the various resources and their quantities within the celestial

    @attr infrastructure: a list of infrastructure tuples on or oribiting the celestial. length is determined on construction. dependent on subclass,
    can either affect global production, pop growth, research, or military (the system will not make this distinction but i do)
    
    @attr category: a string indicating the celestials category,
    if a planet object category will either be (terrestial, gas_giant, or dwarf) 
    if a star will either be (main_sequence, black_hole, giant, white_dwarf, neutron). Otherwise will be (asteroid, comet, or moon)

    @attr population: an integer indicating population size
    @attr habitability: a float indicating percentage of habitability will determine necessary infrastructure / research to enable populations

    @method init_celestials: generate the array of celestials, exists to be overwritten
    @method init resources: initalize the resource pool of the celestial exists to be overwritten
    @method init_buildings: initalize the buildings on or oribting the celestials

    note: we will only handle movement between solar systems. Stars will have a node attribute which serves as a reference to its position in the graph (galaxy)
    '''

    def __init__(self):
        self.celestials = []
        self.resources = {}
        self.infrastructure = []
        self.category = ''

        self.population = 0
        self.habitability = 0.0
    
    celestials = []
    resources = {}
    infrastructure = []
    category = ''

    population = 0
    habitability = 0.0
    

    def moon(self):
        self.celestials = [None]
        self.resources = {}
        self.infrastructure = []
        self.category = 'moon'
        self.population = 0
        self.habitability = choices([0.0,0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], \
            [0.6,0.2,0.05,0.025, 0.025,0.025, 0.025,0.025,0.15, 0.005,0.005])[0]
    
    def asteroid(self):
        self.celestials = [None]
        self.resources = {}
        self.infrastructure = []
        self.category = 'asteroid'
        self.population = 0
        self.habitability = 0
    
    def comet(self):
        self.celestials = [None]
        self.resources = {}
        self.infrastructure = []
        self.category = 'comet'
        self.population = 0
        self.habitability = 0

    def init_celestials(self):
        pass

    def init_resources(self):
        pass
    
    
    def init_buildings(self):
        pass
    
    def set_habitability(self, h = 0):
        self.habitability = h

    def get_celestials(self):
        return self.celestials
    def get_resources(self):
        return self.resources
    def get_infrastructure(self):
        return self.infrastructure
    def get_category(self):
        return self.category
    def get_population(self):
        return self.population
    def get_habitability(self):
        return self.habitability




class Planet(Celestial):
    '''


    @method init_celestials: generate the array of moons oribiting planet (capped for ter)
    @method init_resources: generate the dictionary of resources given the planet type.
    (note: gas giants will randomly generate conditionally on determined presets separate from terrestrials and dwarfs)
    '''
    
    def __init__(self):
        self.category = choices(['terrestial', 'jovian', 'dwarf'], [.425, .525,.05])[0]

        x = 0
        self.celestials = []
        if self.category == 'terrestial':
            x = randint(0,2)
        elif self.category == 'jovian':
            x = randint(0,6)
        else:
            x = randint(0,1)
        
        for i in range(x):
            m = Celestial()
            m.moon()
            self.celestials.append(m)
        
        


    

class Star(Celestial):
    '''
    @attr Node: string indicating node name in the graph (galaxy)
    
    

    @method adjacent_dist: returns floating point distance between this and an adjacent node. used in conjunction with VNMs to enable travel. 
    @method init_celestials:
    @method init_resources:
    @method __init_category:
    

    '''
    def __init__(self, c = None):
        
        if c == None:
            self.category = choices(['main_sequence', 'binary', 'giant', 'dwarf', 'neutron', 'blackhole', 'pulsar',],\
                [.75, .1, .05, .05, .02, .02, .01])[0]
        else:
            self.category = 'quasar'

        x = 0
        self.celestials = [] 
        if self.category == 'main_sequence':
            x = randint(2, 10)
        elif self.category == 'binary':
            x = randint(2, 8)
        elif self.category == 'giant':
            x = randint(1, 3)
        elif self.category == 'dwarf':
            x = randint(2, 8)
        elif self.category == 'neutron':
            x = 0
        elif self.category == 'blackhole':
            x = randint(2,10)
        elif self.category == 'pulsar':
            x = 0
        elif self.category == 'quasar':
            x = 0

        for i in range(x):
            
            h = 0
            new_planet = Planet()
            
            def randhabit():
                return choices([.0, .1, .2, .3, .4, .5, .6, .7, .8, .9, .1], \
                        [.5, .1, .1, .1,  .05, .05, .025, .025, .02, .02, .1])[0]

            if self.category == 'main_sequence':
                h = randhabit()
                new_planet.set_habitability(h)
                self.celestials.append(new_planet)
            
            elif self.category == 'binary':
                h = randhabit()
                new_planet.set_habitability(h)
                self.celestials.append(new_planet)
            
            elif self.category[0] == 'giant':
                new_planet.set_habitability(h)
                self.celestials.append(new_planet)
            
            elif self.category == 'dwarf':
                h = randhabit()
                new_planet.set_habitability(h)
                self.celestials.append(new_planet)
            
            elif self.category == 'neutron':
                continue
                
            elif self.category == 'blackhole':
                new_planet.set_habitability(h)
                self.celestials.append(new_planet)
            
            elif self.category == 'pulsar':
                continue
            
            elif self.category == 'quasar':
                continue
   
        for i in range(randint(0,3)):
                x = randint(0,1)
                a = Celestial()
                if self.celestials == []:
                    if x == 0:
                        a.asteroid()
                        self.celestials.append(a)
                    else:
                        a.comet()
                        self.celestials.append(a)

                else:
                    if x == 0:
                        a.asteroid()
                        self.celestials.insert(randint(0, len(self.celestials)-1), a)
                    else:
                        a.comet()
                        self.celestials.insert(randint(0, len(self.celestials)-1), a)
        
        self.node_name = ''

    def setNodeName(self, node):
        self.node_name = node
    def getNodeName(self):
        return self.node_name 



