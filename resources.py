from random import choices
from random import randint
from random import uniform

class Resources:
    '''
    Here are a list of available resources:
    
    Genetics
    
    Synthetics
    
    Organics
    
    Metals
    
    Fuels
    
    Science

    '''
    resources = {}
    

    
    def __init__(self):
        def init_resource(self, x = 'genetics'):
            self.resources[x] = {"supply": 0, "consumption": 0}

        init_resource(self, x = 'genetics')
        init_resource(self, x = 'synthetics')
        init_resource(self, x = 'organics')
        init_resource(self, x = 'metals')
        init_resource(self, x = 'fuels')
        init_resource(self, x = 'science')



