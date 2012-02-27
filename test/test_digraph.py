# invoke path ceremony!
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import unittest

from digraphing import Digraph, NodeError

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

class DigraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = dummy_graph()

    def testAddAnArc(self):
        a = "A"
        b = "Z"
        self.graph.addArc(a, b)
        self.assertTrue(self.graph.has_arc(a, b))

    def testRemoveAnArc(self):
        self.graph.removeArc("A", "D")

        self.assertTrue(self.graph.has_arc("D", "C"))
        self.assertTrue(self.graph.has_arc("A", "B"))
        self.assertTrue(self.graph.has_arc("B", "C"))
        self.assertFalse(self.graph.has_arc("A", "D"))
    
    def testRemoveNonexistentArc(self):
        self.assertRaises(NodeError, self.graph.removeArc, "A", "Z")

    def testCompressDummyGraph(self):
        compressedGraph = self.graph.compress()

        self.assertTrue(compressedGraph.has_arc("A", "C"))
        self.assertEqual(2, compressedGraph.nodeCount())

    def testCompressBetterGraph(self):
        compressedGraph = better_graph().compress()
        
        self.assertTrue(compressedGraph.has_arc("B", "D"))
        self.assertTrue(compressedGraph.has_arc("D", "E"))
        self.assertTrue(compressedGraph.has_arc("E", "F"))
        self.assertTrue(compressedGraph.has_arc("E", "G"))
        self.assertTrue(compressedGraph.has_arc("G", "H"))
        self.assertTrue(compressedGraph.has_arc("G", "A"))

        self.assertEqual(6, compressedGraph.nodeCount())

if __name__ == "__main__":
    unittest.main()
