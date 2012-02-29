import test_helper
import unittest
from digraphing import Digraph, NodeError

class DigraphTests(test_helper.BaseTest):
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

if __name__ == "__main__":
    unittest.main()
