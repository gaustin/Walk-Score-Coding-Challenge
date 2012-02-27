class Digraph:
    def __init__(self):
        self.graph = dict()

    def addEdge(self, fromNode, toNode):
        if not self.graph.has_key(fromNode):
            self.graph[fromNode] = set() 
        if not self.graph.has_key(toNode):
            self.graph[toNode] = set() 
        
        self.graph[fromNode].add(toNode)

    def removeEdge(self, fromNode, toNode):
        if not self.graph.has_key(fromNode) or not self.graph.has_key(toNode):
            raise NodeError("A given node does not exist in the graph.")
        
        # Delete the node
        self.graph[fromNode].discard(toNode)

    def has_arc(self, fromNode, toNode):
        return toNode in self.graph[fromNode]

    def adjacent(self, aNode, bNode):
        if bNode in self.graph[aNode] or aNode in self.graph[bNode]:
            return True
        else:
            return False

class NodeError(Exception):
    def __init__(self, message):
        self.message = message

