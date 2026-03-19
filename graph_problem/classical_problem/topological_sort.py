#  Kahns algorithm is another way of doing Topological sort

import sys

sys.setrecursionlimit(200000)

def solve():
    # ... (Assume adj and n are initialized from input) ...
    
    visited = [False] * (n + 1)
    topo_order = []

    def dfs(u):
        visited[u] = True
        
        # Explore all dependencies first
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        
        # THE TWEAK: Add to list ONLY after all neighbors are finished
        topo_order.append(u)

    # Call DFS for all components
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    # The result is the reverse of the finishing order
    print("Topological Sort:", topo_order[::-1])