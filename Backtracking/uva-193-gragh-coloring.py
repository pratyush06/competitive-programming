import copy
class Vertex:
    def __init__(self,vertex_no):
        self.edges=set()
        self.vertex_no=vertex_no

    def addEdge(self, b):
        self.edges.add(b)
    def hasNeighbour(self, c):
        if c in self.edges:
            return True
        return False

def place(k, curr, visited):
    if k.vertex_no in curr:
        return False
    visited[k]=True
    for m in curr:
        if k.hasNeighbour(m):
            return False
    return True

def backtrack(list_of_vertex, curr=None, ans=None, visited=None):
    if visited is None:
        visited={}
    if curr is None:
        curr=[]
    if ans is None:
        ans=[]
    # exit condition
    if len(visited)==len(list_of_vertex):
        ans.append(copy.copy(curr))


    # for loop
    for i, k in list_of_vertex.items():
        if place(k, curr, visited):
            curr.append(i)
            ans = backtrack(list_of_vertex, curr, ans, visited)
            curr.pop()
    
    return ans



no_of_gragh = int(input())

for _ in range(no_of_gragh):
    no_of_vertex, no_of_edges = map(int, input().split(" "))
    list_of_vertex = {}
    for j in range(1, no_of_vertex+1):
        list_of_vertex[j]=Vertex(j)
    for k in range(no_of_edges):
        source, destination = map(int, input().split(" "))
        list_of_vertex[source].addEdge(destination)
        list_of_vertex[destination].addEdge(source)
    print(backtrack(list_of_vertex))
    