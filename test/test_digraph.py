# invoke path ceremony!
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import unittest

from digraphing import Digraph, NodeError

def dummy_graph():
    # A B
    # B C
    # A D 
    # D C
    graph = Digraph()
    graph.addEdge("A", "B")
    graph.addEdge("B", "C")
    graph.addEdge("A", "D")
    graph.addEdge("D", "C")
    return graph

class DigraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = dummy_graph()

    def testAddAnEdge(self):
        a = "A"
        b = "Z"
        self.graph.addEdge(a, b)
        self.assertTrue(self.graph.has_arc(a, b))

    def testRemoveAnEdge(self):
        self.graph.removeEdge("A", "D")

        self.assertTrue(self.graph.has_arc("D", "C"))
        self.assertTrue(self.graph.has_arc("A", "B"))
        self.assertTrue(self.graph.has_arc("B", "C"))
        self.assertFalse(self.graph.has_arc("A", "D"))
    
    def testRemoveNonexistentEdge(self):
        self.assertRaises(NodeError, self.graph.removeEdge, "A", "Z")

if __name__ == "__main__":
    unittest.main()
