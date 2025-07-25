# Note: apart from ajanjacny matrix and list there is implicit graph which we calculated don't require them to store(edges can be determine with some rule)

import sys
class Vertex:
    def __init__(self, node):
        self.id=node
        self.adjacent = {}
        # self.distance = sys.maxint
        self.visited = False
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor]=weight
    
    def getConnections(self):
        return self.adjacent.keys()
    
    def getVertex_ID(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
    
    def setDistance(self, dist):
        self.distance=dist
    
    def getDistance(self):
        return self.distance
    
    def setPrevious(self, prev):
        self.previous=prev
    
    def setVisited(self):
        self.visited=True
    
    def __str__(self):
        return str(self.id) + 'adjacent' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0
    
    def __iter__(self):
        return iter(self.vertDictionary.values())
    
    def addVertex(self, node):
        self.numVertices+=1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None
    
    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)
        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
    
    def getVertices(self):
        return self.vertDictionary.keys()
    
    def getEdges(self):
        edges = []
        for v in self.vertDictionary.values():
            for w in v.getConnections():
                vid = v.getVertex_ID()
                wid = w.getVertex_ID()
                edges.append((vid, wid, v.getWeight(w)))
        
        return edges



if __name__=="__main__":
    G=Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a', 'b', 4)
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 4)
    G.addEdge('d', 'e', 4)

    print("Gragh Data")
    print(G.getEdges())

