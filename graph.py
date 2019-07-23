# Wossen Hailemariam
class Graph:
    def __init__(self):
        self.numNodes = 0
        self.out = {}
        self.inc = {}

    def addNode(self, val):
        # add node
        if not (val in self.out or val in self.inc):
            self.out[val] = []
            self.inc[val] = []
            self.numNodes += 1
        else:
            print("Node already exists.")

    def addEdge(self, fromNode, toNode, weight):
        # add edge to outgoing
        if (fromNode in self.out):
            values = self.out[fromNode]
            if toNode in values:
                print("Edge already exists.")
            else:
                values.append((toNode, weight))
                values.sort()
                self.out[fromNode] = values
        else:
            print("Node does not exist.")
        # add edge to incoming
        if (toNode in self.inc):
            values = self.inc[toNode]
            if fromNode in values:
                print("Edge already exists.")
            else:
                values.append((fromNode, weight))
                values.sort()
                self.inc[toNode] = values
        else:
            print("Node does not exist.")

    def getEdge(self, i, j):
        # return weight
        if (i in self.out):
            values = self.out[i]
            for (node,weight) in values:
                if (node == j):
                    return weight
        return None

    def allEdges(self):
        nodes = self.allNodes()
        edges = []
        # for each node, get all outgoing nodes
        for node in nodes:
            toNodesRaw = self.outgoing(node)
            toNodes = []
            # for each outgoing (toNode, weight), extract toNode,
            # then add (node, toNode) to the edges
            for n in toNodesRaw:
                (toNode, weight) = n
                edges.append((node,toNode,weight))
        return edges

    def allNodes(self):
        res = []
        for e in self.out.keys():
            res.append(e)
        return res

    def incoming(self, toNode):
        # return List(fromNode, weight)
        if (toNode in self.inc):
            return self.inc[toNode]
        else:
            print("Node does not exist")

    def outgoing(self, fromNode):
        # return List(toNode, weight)
        if (fromNode in self.out):
            return self.out[fromNode]
        else:
            print("Node does not exist")

def makeGraph():
    g = Graph()
    nodes = [1,2,3,4,5,7,12,14,17,22,53]
    for n in nodes:
        g.addNode(n)
    edges = {2:[4], 3:[2,3,7], 4:[1,2,17], 5:[2], 12:[4,22], 14:[1,12,53],
                22:[14], 53:[14], 17:[3,4,5]}
    for fromNode, toNodes in edges.items():
        for toNode in toNodes:
            g.addEdge(fromNode, toNode, 1)
    return g

def makeUndirectedGraph():
    g = Graph()
    nodes = [1,2,3,4,5,7,12,14,17,22,53]
    for n in nodes:
        g.addNode(n)
    edges = {2:[4], 3:[2,3,7], 4:[1,17], 5:[2], 12:[4,22], 14:[1,12,53],
                22:[14], 17:[3,5]}
    for fromNode, toNodes in edges.items():
        for toNode in toNodes:
            g.addEdge(fromNode, toNode, 1)
            g.addEdge(toNode, fromNode, 1)
    return g

def makeOtherUndirectedGraph():
    g = Graph()
    nodes = [0,1,3,2,4,5]
    for n in nodes:
        g.addNode(n)
    g.addEdge(0,1,10)
    g.addEdge(1,0,10)
    g.addEdge(1,3,5)
    g.addEdge(3,1,5)
    g.addEdge(1,2,10)
    g.addEdge(2,1,10)
    g.addEdge(2,4,7)
    g.addEdge(4,2,7)
    g.addEdge(3,4,5)
    g.addEdge(4,3,5)
    g.addEdge(4,5,15)
    g.addEdge(5,4,15)
    return g
