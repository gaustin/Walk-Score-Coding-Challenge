import test_helper
import unittest

from digraphing import GraphProcessor

class GraphProcessorTests(test_helper.BaseTest):
    def testCompressDummyGraph(self):
        self.gp.compressInPlace(self.graph)

        self.assertTrue(self.graph.has_arc("A", "C"))
        self.assertEqual(2, self.graph.nodeCount())

    def testCompressBetterGraph(self):
        betterGraph = test_helper.better_graph()
        self.gp.compressInPlace(betterGraph)
        
        self.assertTrue(betterGraph.has_arc("B", "D"))
        self.assertTrue(betterGraph.has_arc("D", "E"))
        self.assertTrue(betterGraph.has_arc("E", "F"))
        self.assertTrue(betterGraph.has_arc("E", "G"))
        self.assertTrue(betterGraph.has_arc("G", "H"))
        self.assertTrue(betterGraph.has_arc("G", "B"))

        self.assertEqual(6, betterGraph.nodeCount())


if __name__ == "__main__":
    unittest.main()
