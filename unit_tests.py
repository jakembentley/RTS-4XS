from rts4xs_objects import Countable
from celestials import Celestial
from celestials import Star
from celestials import Planet
import unittest
from galaxy import Node
from galaxy import Galaxy

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
        
class testNode(unittest.TestCase):
    def testAddEdge(self):
        n = Node()
        n2 = Node()
        n.addEdge(n2, 2)
        self.assertEqual(n.edges, [(n2, 2)])
        self.assertEqual(n2.edges, [(n, 2)])





if __name__ == "__main__":
    unittest.main()
