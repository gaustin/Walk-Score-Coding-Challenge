import test_helper
import unittest

class GraphProcessor(test_helper.BaseTest):
    def testCompressDummyGraph(self):
        compressedGraph = self.graph.compress()

        self.assertTrue(compressedGraph.has_arc("A", "C"))
        self.assertEqual(2, compressedGraph.nodeCount())

    def testCompressBetterGraph(self):
        compressedGraph = test_helper.better_graph().compress()
        
        self.assertTrue(compressedGraph.has_arc("B", "D"))
        self.assertTrue(compressedGraph.has_arc("D", "E"))
        self.assertTrue(compressedGraph.has_arc("E", "F"))
        self.assertTrue(compressedGraph.has_arc("E", "G"))
        self.assertTrue(compressedGraph.has_arc("G", "H"))
        self.assertTrue(compressedGraph.has_arc("G", "B"))

        self.assertEqual(6, compressedGraph.nodeCount())

if __name__ == "__main__":
    unittest.main()
