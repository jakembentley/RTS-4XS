from random import choices
from random import randint
from random import random
import celestials as c
import networkx as nx
from uuid import uuid4
import math

class Node:
    def __init__(self):
        self.nodeName = uuid4().hex
        self.edges = []
        self.parent = None
        self.star = None
    
    def addEdge(self, node, w):
        edge = (node, w)
        other = (self, w)
        self.edges.append(edge)
        node.edges.append(other)
    
    def randomNode(self):
        self.nodeName = uuid4().hex
        self.star = c.Star()

class Galaxy:
    def __init__(self):
        self.center = None
        self.graph_dict = {}
    
    def addNode(self, node):
        '''control against adding nodes already present, node should be fully initialized before calling this method'''
        if node not in self.graph_dict:
            self.graph_dict[node.nodeName] = Node()

    def setCenter(self):
        self.center = Node()
        self.center.star = c.Star(c = 'quasar')
        
    
    def randomWeight(self):
        return randint(0,6) + random()

    def firstNode(self):
        '''
        must have initalized the center
        '''
        og_node = Node()
        og_node.parent = self.center
        og_node.addEdge(self.center, self.randomWeight())
        og_node.randomNode()


        


    


    



    


    

        


        




