import sys
from collections import deque

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = int(next(it)), int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        
    # -1: Uncolored, 0: Color A, 1: Color B
    color = [-1] * (n + 1)

    def is_bipartite_bfs(start_node):
        queue = deque([start_node])
        color[start_node] = 0 # Start with color 0
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if color[v] == -1:
                    # Color with the opposite: if u is 0, v becomes 1; if u is 1, v becomes 0
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    # Conflict found! Same color neighbors.
                    return False
        return True

    # Check every connected component
    possible = True
    for i in range(1, n + 1):
        if color[i] == -1:
            if not is_bipartite_bfs(i):
                possible = False
                break
                
    if possible:
        print("YES, the graph is Bipartite.")
    else:
        print("NO, the graph is not Bipartite.")

if __name__ == "__main__":
    solve()