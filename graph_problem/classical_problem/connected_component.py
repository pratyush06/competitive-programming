# connected component problem can also be solved using union find as well and so with dfs and bfs

import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    n = int(next(it)) # Number of nodes
    m = int(next(it)) # Number of edges
    
    # 1. Build Adjacency List from Edge List input
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = int(next(it)), int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (n + 1)
    all_components = []

    # 2. The standard DFS signature
    def dfs(u, current_component):
        visited[u] = True
        current_component.append(u)
        
        for v in adj[u]:
            if not visited[v]:
                dfs(v, current_component)

    # 3. Iterate through all nodes to find each component
    for i in range(1, n + 1):
        if not visited[i]:
            # Found a new component!
            component = []
            dfs(i, component)
            all_components.append(component)

    # 4. Output results
    print(f"Total Connected Components: {len(all_components)}")
    for idx, comp in enumerate(all_components, 1):
        print(f"Component {idx}: {comp}")

if __name__ == "__main__":
    solve()