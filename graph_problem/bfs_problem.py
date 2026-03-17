## if Input is given as edge list first convert that to adj list or matrix and than try to solve problem using bfs or dfs other complexity can be O(V^3) as to look for all connection of node 1 we have to traverse entire edge list and we will do that for all the nodes so it's to complex

import sys
from collections import deque

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    
    # Reading N (nodes) and M (edges)
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration:
        return
    
    # Adjacency List (1-based indexing)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * (n + 1)
    # distance[i] can store the shortest path distance from start node to i
    distance = [-1] * (n + 1)
    traversal_path = []

    # The BFS Signature: matches "void bfs(int s)"
    def bfs(start_node):
        queue = deque([start_node])
        visited[start_node] = True
        distance[start_node] = 0 # Distance to self is 0
        
        while queue:
            u = queue.popleft() # Dequeue the front node
            traversal_path.append(u)
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u] + 1 # Level tracking
                    queue.append(v) # Enqueue the neighbor

    # Handle disconnected components
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            
    print("BFS Traversal Order:", " ".join(map(str, traversal_path)))
    # Optional: print distances from the first node
    # print("Distances:", distance[1:])

if __name__ == "__main__":
    solve()