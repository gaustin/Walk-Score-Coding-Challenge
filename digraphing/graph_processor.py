from digraphing import Digraph

class GraphProcessor:
    def removeListOfNodes(self, graph, listOfNodes=None):
        if listOfNodes is None:
            listOfNodes = list()

        for node in listOfNodes:
            graph.removeNode(node)

        for node, outArcs in graph.items():
            outArcs.difference_update(listOfNodes)
 
    def compressInPlace(self, graph):
        nodesToPrune = dict() 
        for node, outArcs in graph.items():
            inArcs = graph.inArcs(node)
            if len(outArcs) == 1 and len(inArcs) == 1:
                nodesToPrune[node] = { 'in': inArcs, 'out': outArcs }

        for node, arcPair in nodesToPrune.items():
            fromArc = arcPair['in'].pop()
            toArc = arcPair['out'].pop()
            graph.addArc(fromArc, toArc)
            self.removeListOfNodes(graph, nodesToPrune)

