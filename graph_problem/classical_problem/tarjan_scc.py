class TarjanSCC:
    def __init__(self, n):
        """
        Initializes the graph for Tarjan's Algorithm.
        :param n: Number of vertices (0 to n-1)
        """
        self.n = n
        self.adj = [[] for _ in range(n)]
        
        # State variables for the algorithm
        self.timer = 0
        self.disc = []
        self.low = []
        self.in_stack = []
        self.stack = []
        self.sccs = []

    def add_edge(self, u, v):
        """Adds a directed one-way edge from u to v."""
        self.adj[u].append(v)

    def _dfs(self, u):
        """Internal recursive DFS function to explore components."""
        self.disc[u] = self.timer
        self.low[u] = self.timer
        self.timer += 1
        
        self.stack.append(u)
        self.in_stack[u] = True

        # Explore all outgoing edges
        for v in self.adj[u]:
            if self.disc[v] == -1:  
                # Tree Edge: Node v is completely unvisited
                self._dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
                
            elif self.in_stack[v]:  
                # Back/Cross Edge: Node v is visited AND part of the active path
                self.low[u] = min(self.low[u], self.disc[v])

        # Root Check: If u is the "entry point" of the SCC
        if self.low[u] == self.disc[u]:
            current_scc = []
            
            # Extract everything from the stack up to u
            while True:
                v = self.stack.pop()
                self.in_stack[v] = False  # Remove from active tracking
                current_scc.append(v)
                if u == v:
                    break
                    
            self.sccs.append(current_scc)

    def get_components(self):
        """
        Executes the algorithm and returns the Strongly Connected Components.
        """
        # Reset state in case the method is called multiple times on the same object
        self.timer = 0
        self.disc = [-1] * self.n
        self.low = [-1] * self.n
        self.in_stack = [False] * self.n
        self.stack = []
        self.sccs = []

        # Run DFS from every node to ensure disconnected components are found
        for i in range(self.n):
            if self.disc[i] == -1:
                self._dfs(i)

        return self.sccs


# --- Example Usage ---
if __name__ == "__main__":
    # Create a graph with 5 nodes (0 to 4)
    # SCC 1: 0 -> 1 -> 2 -> 0
    # Cross Edge: 1 -> 3
    # SCC 2: 3 -> 4 -> 3
    graph = TarjanSCC(5)
    
    # Add directed edges
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 3)]
    for u, v in edges:
        graph.add_edge(u, v)

    # Get the results
    components = graph.get_components()
    
    print("Strongly Connected Components:")
    for i, scc in enumerate(components):
        print(f"SCC {i + 1}: {scc}")