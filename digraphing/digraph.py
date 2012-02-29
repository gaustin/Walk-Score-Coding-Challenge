class Digraph:
    def __init__(self):
        self.graph = dict()

    def addArc(self, fromNode, toNode):
        if not self.graph.has_key(fromNode):
            self.graph[fromNode] = set() 
        if not self.graph.has_key(toNode):
            self.graph[toNode] = set() 
        
        self.graph[fromNode].add(toNode)

    def removeArc(self, fromNode, toNode):
        if not self.graph.has_key(fromNode) or not self.graph.has_key(toNode):
            raise NodeError("A given node does not exist in the graph.")
        
        # Delete the arc
        self.graph[fromNode].discard(toNode)

    def removeNode(self, node, cascade=False):
        if self.graph.has_key(node):
            del self.graph[node]

    def addOrUpdateNode(self, node, outArcs=None):
        if outArcs is None:
            outArcs = set()

        if self.graph.has_key(node):
            outArcs = outArcs.union(self.graph[node])

        self.graph[node] = outArcs

    def removeListOfNodes(self, listOfNodes=None):
        if listOfNodes is None:
            listOfNodes = list()

        for node in listOfNodes:
            self.removeNode(node)

        for node, outArcs in self.graph.items():
            outArcs.difference_update(listOfNodes)
 
    def compressInPlace(self):
        prunedNodes = set()
        for node, outArcs in self.graph.items():
            print self.graph
            in_arcs = self.inArcs(node)
            if len(outArcs) == 1 and len(in_arcs) == 1:
                fromArc = in_arcs.pop()
                toArc = outArcs.copy().pop()
                self.addArc(fromArc, toArc)
                prunedNodes.add(node)

        self.removeListOfNodes(prunedNodes)

    def compress(self):
        # Non-destructive
        compressedGraph = Digraph()
        prunedNodes = set()
        for node, outArcs in self.graph.items():
            in_arcs = self.inArcs(node)
            if len(outArcs) == 1 and len(in_arcs) == 1:
                prunedNodes.add(node)
                fromArc = in_arcs.pop()
                toArc = outArcs.copy().pop()
                compressedGraph.addArc(fromArc, toArc) 
            else:
                arcs = outArcs.difference(prunedNodes)
                compressedGraph.addOrUpdateNode(node, arcs)

        # Remove all of the pruned nodes
        compressedGraph.removeListOfNodes(prunedNodes) 

        return compressedGraph

    def inArcs(self, targetNode):
        # Return all of the arcs pointing at this node
        in_arcs = set()
        for node, outArcs in self.graph.items():
            if targetNode in outArcs:
                in_arcs.add(node)

        return in_arcs

    def has_arc(self, fromNode, toNode):
        if not self.graph.has_key(fromNode):
            return False
        return toNode in self.graph[fromNode]

    def adjacent(self, aNode, bNode):
        if bNode in self.graph[aNode] or aNode in self.graph[bNode]:
            return True
        else:
            return False

    def nodeCount(self):
        return len(self.graph.keys())

class NodeError(Exception):
    def __init__(self, message):
        self.message = message

