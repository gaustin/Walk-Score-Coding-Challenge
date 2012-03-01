class Digraph:
    def __init__(self):
        self.graph = dict()

    def items(self):
        return self.graph.items()

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

    def inArcs(self, targetNode):
        # Return all of the arcs pointing at this node
        inArcs = set()
        for node, outArcs in self.graph.items():
            if targetNode in outArcs:
                inArcs.add(node)

        return inArcs

    def outArcs(self, targetNode):
        if self.graph.has_key(targetNode):
            return self.graph[targetNode]
        else:
            return set()

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

