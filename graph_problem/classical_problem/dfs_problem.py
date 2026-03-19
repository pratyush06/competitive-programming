## if Input is given as edge list first convert that to adj list or matrix and than try to solve problem using bfs or dfs other complexity can be O(V^3) as to look for all connection of node 1 we have to traverse entire edge list and we will do that for all the nodes so it's to complex

import sys

# 1. Increase recursion depth (essential for deep trees/graphs)
sys.setrecursionlimit(200000)

def solve():
    # 2. Fast I/O: Reading all input at once is much faster than multiple input() calls
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    
    # Read N (nodes) and M (edges)
    n = int(next(it))
    m = int(next(it))
    
    # 3. Adjacency List Initialization
    # Using n+1 to handle 1-based indexing common in CP problems
    adj = [[] for _ in range(n + 1)]
    
    # 4. Build the Graph
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # Undirected graph: add both directions
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * (n + 1)
    traversal_path = []

    # 5. The DFS Signature: matches "void dfs(int u)"
    def dfs(u):
        visited[u] = True
        traversal_path.append(u) # Example: record the order of visit
        
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    # 6. Handle Disconnected Graphs
    # Ensure we visit every component
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            
    # Output the result
    print("DFS Traversal Order:", " ".join(map(str, traversal_path)))

if __name__ == "__main__":
    solve()