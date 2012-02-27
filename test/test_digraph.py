# invoke path ceremony!
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import unittest

from digraphing import Digraph

class DigraphTests(unittest.TestCase):
    def testAddSingleEdge(self):
        graph = Digraph()
        a = "A"
        b = "B"
        graph.addEdge(a, b)
        self.assertTrue(graph.adjacent(a, b))

if __name__ == "__main__":
    unittest.main()
