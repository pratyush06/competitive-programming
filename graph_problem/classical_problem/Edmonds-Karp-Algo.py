from collections import deque

def bfs(residual_graph, source, sink, parent):
    """Finds an augmenting path using BFS."""
    visited = [False] * len(residual_graph)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        # Look at all possible neighbors v
        for v, capacity in enumerate(residual_graph[u]):
            if not visited[v] and capacity > 0:
                parent[v] = u
                visited[v] = True
                if v == sink:
                    return True
                queue.append(v)
    return False

def edmonds_karp(capacity_matrix, source, sink):
    """Calculates Maximum Flow from source to sink."""
    n = len(capacity_matrix)
    # The residual graph starts as a copy of the original capacities
    residual = [row[:] for row in capacity_matrix]
    parent = [-1] * n
    max_flow = 0
    
    # Step 1: Keep searching for augmenting paths
    while bfs(residual, source, sink, parent):
        # Step 2: Find the bottleneck (minimum capacity) on this path
        path_flow = float('inf')
        s = sink
        while s != source:
            u = parent[s]
            path_flow = min(path_flow, residual[u][s])
            s = parent[s]
            
        # Step 3: Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow # Forward edge
            residual[v][u] += path_flow # Backward edge
            v = parent[v]
            
        max_flow += path_flow
        
    return max_flow