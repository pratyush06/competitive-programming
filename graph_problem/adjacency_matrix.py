# The adjacency matrix representation is good if the graphs are dense. The matrix requires O(V^2) bits of storage and O(V^2) time for 
# initialization. If the number of edges is proportional to V , then there is no problem because V steps are required to read the edges. If the 
# graph is sparse, the initialization of the matrix dominates the running time of the algorithm as it takes takes O(V^2 ).  
 
# Another drawback of Adjacency Matrix is that it also takes O(V) time to enumerate the list of neighbors of a vertex v, 
# and the O(V ) space cost is high for sparse graphs, those with much fewer than V edges. 
 
# The adjacency matrix representation takes O( V^2 ) amount of space while it is computed. When graph has maximum number of edges or 
# minimum number of edges, in both cases the required space will be same.
# general rule of thumb use adjancecy matrix if V is less than or equal to 1000 

class Vertex:
    def __init__(self, node):
        self.id=node
        self.visited=False
    
    def setVertex_ID(self, id):
        self.id=id
    def getVertex_ID(self):
        return self.id
    def setVisited(self):
        self.visited=True
    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self, numVertices, cost=0):
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices=numVertices
        self.Vertices = []
        for i in range(numVertices):
            newVertex = Vertex(i)
            self.Vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0<=vtx<self.numVertices:
            self.Vertices[vtx].setVertex_ID(id)

    def getVertex(self, n):
        for vertx in range(self.numVertices):
            if n==self.Vertices[vertx].getVertex_ID():
                return vertx
        else:
            return -1

    def addEdge(self, frm, to, cost):
        if self.getVertex(frm)!=-1 and self.getVertex(to)!=-1:
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)]=cost
            #For directed graph do not add this 
            # self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        vertices = []
        for vtx in range(self.numVertices):
            vertices.append(self.Vertices[vtx].getVertex_ID())

        return vertices

    def printMatrix(self):
        # import pdb;pdb.set_trace()
        for u in range(self.numVertices):
            row = []
            for v in range(self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        # import pdb;pdb.set_trace()
        for v in range(self.numVertices):
            for u in range(self.numVertices):
                if self.adjMatrix[u][v]!=-1:
                    vid = self.Vertices[v].getVertex_ID()
                    wid = self.Vertices[u].getVertex_ID()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges


if __name__=='__main__':
    G = Graph(5)
    G.setVertex(0,'a') 
    G.setVertex(1, 'b') 
    G.setVertex(2, 'c') 
    G.setVertex(3, 'd') 
    G.setVertex(4, 'e') 
    print ('Graph data:')  
    G.addEdge('a', 'e', 10)   
    G.addEdge('a', 'c', 20) 
    G.addEdge('c', 'b', 30) 
    G.addEdge('b', 'e', 40) 
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60) 
    print (G.printMatrix())       
    print (G.getEdges()) 
