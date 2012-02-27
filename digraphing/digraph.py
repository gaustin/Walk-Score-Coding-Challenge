class Digraph:
    def __init__(self):
        self.graph = dict()

    def addEdge(self, fromNode, toNode):
        if not self.graph.has_key(fromNode):
            self.graph[fromNode] = set() 
        if not self.graph.has_key(toNode):
            self.graph[toNode] = set() 
        
        self.graph[fromNode].add(toNode)

    def adjacent(self, aNode, bNode):
        if bNode in self.graph[aNode] or aNode in self.graph[bNode]:
            return True
        else:
            return False
