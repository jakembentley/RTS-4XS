from rts4xs_objects import Countable
from celestials import Celestial
from celestials import Star
from celestials import Planet
import unittest


class testCountable(unittest.TestCase):

    def testIncrementCountable(self):
        c = Countable()
        e = c.getElement()
        c.increment(v = 1)
        self.assertGreater(c.getElement(), e)

class testCelestial(unittest.TestCase):
    
    def testCelestial(self):
        c = Celestial()
        self.assertIsInstance(c, Celestial)

    def testStar(self):
        s = Star()
        self.assertIsInstance(s, Star)

    def testCelestials(self):
        '''asserts that a star is accurately initalizing celestials'''
        s = Star()
        for i in range(len(s.celestials)):
            self.assertIsInstance(s.celestials[i],  Celestial)
    
    def testStarCategory(self):
        s = Star()
        self.assertIn(s.category, ['main_sequence', 'blackhole', 'pulsar', 'dwarf', 'giant', 'neutron', 'binary', 'quasar'])
        
if __name__ == "__main__":
    unittest.main()
