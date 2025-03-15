# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew={}
        # return dfs(node, oldToNew) if node else None
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy=Node(node.val)
            oldToNew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) 
            return copy
        return dfs(node) if node else None

adjList = [[2,4],[1,3],[2,4],[1,3]]

for i in range(1, len(adjList)+1):
    n1=Node(i, adjList)