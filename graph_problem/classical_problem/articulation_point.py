# Think of low[v] as "v's elevator" that can take it up:

# low[v] < disc[u]: Elevator goes ABOVE u → u is replaceable

# low[v] == disc[u]: Elevator only reaches u → u is critical

# low[v] > disc[u]: No elevator! → u is critical AND the connection is a bridge

# Summary Table
# Concept	Meaning	Analogy
# disc[u]	When was u first visited?	"Meeting time"
# low[u]	Earliest discovered node reachable from u	"Oldest ancestor I can reach"
# low[v] > disc[u]	v's subtree can't reach u or above	"Child has no way back up" → Bridge!
# low[v] >= disc[u]	v's subtree can't reach above u	"Child depends on me" → Articulation point!

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.time = 0
        
    def add_edge(self, u, v):
        """Add undirected edge"""
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def find_articulation_points_and_bridges(self):
        """Main method to find both articulation points and bridges"""
        
        # Initialize arrays
        visited = [False] * self.V
        disc = [0] * self.V      # Discovery time
        low = [0] * self.V       # Lowest discovery time reachable
        parent = [-1] * self.V   # Parent in DFS tree
        ap = [False] * self.V    # Articulation points
        bridges = []              # Store bridges
        
        def dfs(u):
            # Mark as visited and set discovery time
            visited[u] = True
            self.time += 1
            disc[u] = low[u] = self.time
            children = 0
            
            for v in self.graph[u]:
                if not visited[v]:
                    children += 1
                    parent[v] = u
                    dfs(v)
                    
                    # After returning from child, update low[u]
                    low[u] = min(low[u], low[v])
                    
                    # Check for articulation point (non-root case)
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                    
                    # Check for bridge
                    if low[v] > disc[u]:
                        bridges.append((u, v))
                
                elif v != parent[u]:  # Back edge
                    low[u] = min(low[u], disc[v])
            
            # Check for articulation point (root case)
            if parent[u] == -1 and children > 1:
                ap[u] = True
        
        # Run DFS for all components
        for i in range(self.V):
            if not visited[i]:
                dfs(i)
        
        return ap, bridges
    
    def print_results(self):
        """Print articulation points and bridges"""
        ap, bridges = self.find_articulation_points_and_bridges()
        
        # Print articulation points
        print("Articulation Points:", end=" ")
        for i in range(self.V):
            if ap[i]:
                print(i, end=" ")
        print()
        
        # Print bridges
        print("Bridges:", end=" ")
        for u, v in bridges:
            print(f"{u}-{v}", end=" ")
        print()


# Example usage
if __name__ == "__main__":
    # Example 1: Graph with articulation points and bridges
    print("=== Example 1 ===")
    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 0)  # Triangle 0-1-2
    g1.add_edge(2, 3)  # Bridge to 3
    g1.add_edge(3, 4)  # Chain to 4
    
    g1.print_results()
    # Expected: Articulation Point: 2, Bridge: 2-3, 3-4