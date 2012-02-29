# invoke path ceremony!
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import unittest

from digraphing import Digraph

def better_graph():
    # A B
    # B C
    # C D
    # B D
    # D E
    # E F
    # E G
    # G H
    # G A
    graph = Digraph()
    graph.addArc("A", "B")
    graph.addArc("B", "C")
    graph.addArc("C", "D")
    graph.addArc("B", "D")
    graph.addArc("D", "E")
    graph.addArc("E", "F")
    graph.addArc("E", "G")
    graph.addArc("G", "H")
    graph.addArc("G", "A")
    return graph

def dummy_graph():
    # A B
    # B C
    # A D 
    # D C
    graph = Digraph()
    graph.addArc("A", "B")
    graph.addArc("B", "C")
    graph.addArc("A", "D")
    graph.addArc("D", "C")
    return graph

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.graph = dummy_graph()


