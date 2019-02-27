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
    
    def moon(self):
        self.celestials = [None]
        self.resources = {}
        self.infrastructure = []
        self.category = 'moon'
        self.population = 0
        self.habitability = choices([0.0,0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], \
            [0.6,0.2,0.05,0.025, 0.025,0.025, 0.025,0.025,0.15, 0.005,0.005]) 
    
    def asteroid(self):
        self.celestials = [None]
        self.resources = {}
        self.infrasture = []
        self.category = 'asteroid'
        self.population = 0
        self.habitability = 0
    
    def comet(self):
        self.celestials = [None]
        self.resources = {}
        self.infrasture = []
        self.category = 'comet'
        self.population = 0
        self.habitability = 0

    def init_celestials(self):
        pass

    def init_resources(self):
        pass
    
    def init_buildings(self):
        pass
    
    

class Planet(Celestial):
    '''


    @method init_celestials: generate the array of moons oribiting planet (capped for ter)
    @method init_resources: generate the dictionary of resources given the planet type.
    (note: gas giants will randomly generate conditionally on determined presets separate from terrestrials and dwarfs)
    '''
    
    def __init__(self):
        self.category = choices(['terrestial', 'jovian', 'dwarf'], [.425, .525,.05])

        x = 0
        self.celestials = []
        if self.category == 'terrestial':
            x = randint(0,2)
        elif self.category == 'jovian':
            x = randint(0,6)
        else:
            x = randint(0,1)
        
        for i in range(x):
            self.celestials.append(Celestial().moon())
        
        


    

class Star(Celestial):
    '''
    @attr Node: string indicating node name in the graph (galaxy)
    
    

    @method adjacent_dist: returns floating point distance between this and an adjacent node. used in conjunction with VNMs to enable travel. 
    @method init_celestials:
    @method init_resources:
    @method __init_category:
    

    '''




