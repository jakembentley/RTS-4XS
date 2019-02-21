
class Countable:
    '''Several in-game elements will require tracking real
    time changes in attributes. Countable objects will feed into
    more complex objects and eventually a GUI. 
    '''
    element = 0
    
    def increment(self):
        element++

    

