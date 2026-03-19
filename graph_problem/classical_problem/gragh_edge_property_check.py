class Graph:
    def __init__(self):
        self.graph = {}
        self.color = {}
        self.discovery = {}
        self.finish = {}
        self.parent = {}  # Track parent in DFS tree
        self.time = 0
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
    
    def dfs_visit(self, node):
        self.color[node] = 'gray'
        self.time += 1
        self.discovery[node] = self.time
        print(f"  ▶ Discovered {node} (time: {self.discovery[node]})")
        
        for neighbor in self.graph.get(node, []):
            print(f"    Edge: {node} → {neighbor}")
            
            if self.color[neighbor] == 'white':
                self.parent[neighbor] = node
                print(f"      ✅ TREE EDGE: exploring {neighbor}")
                self.dfs_visit(neighbor)
            
            elif self.color[neighbor] == 'gray':
                print(f"      🔴 BACK EDGE: creates a cycle!")
            
            elif self.color[neighbor] == 'black':
                if self.discovery[node] < self.discovery[neighbor]:
                    print(f"      ⬆️ FORWARD EDGE: ancestor to descendant")
                else:
                    print(f"      ↔️ CROSS EDGE: different branches")
        
        self.color[node] = 'black'
        self.time += 1
        self.finish[node] = self.time
        print(f"  ◼ Finished {node} (time: {self.finish[node]})")
    
    def dfs(self, start):
        # 1. Initialize all nodes
        for node in self.graph:
            self.color[node] = 'white'
            self.discovery[node] = 0
            self.finish[node] = 0
            self.parent[node] = None
        
        self.time = 0
        print(f"\n🚀 Starting DFS from {start}")
        print("-" * 40)
        
        # 2. Visit the requested start node first
        if start in self.graph:
            self.dfs_visit(start)
            
        # 3. FIX: Check for any disconnected nodes we missed (DFS Forest)
        for node in self.graph:
            if self.color[node] == 'white':
                print(f"\n🌲 Starting new DFS tree from disconnected node: {node}")
                self.dfs_visit(node)
        
        # Print summary
        print("\n" + "=" * 40)
        print("FINAL RESULTS:")
        print("-" * 40)
        print("\nNode timings [Discovery, Finish]:")
        for node in sorted(self.graph.keys()):
            print(f"  {node}: [{self.discovery[node]}, {self.finish[node]}]")
        
        # Classify all edges based on timestamps
        print("\nAll edges classified mathematically:")
        for u in sorted(self.graph.keys()):
            for v in sorted(self.graph[u]):
                # Interval of v is entirely contained within interval of u
                if self.discovery[u] < self.discovery[v] and self.finish[u] > self.finish[v]:
                    if self.parent[v] == u:
                        print(f"  {u} → {v}: TREE EDGE")
                    else:
                        print(f"  {u} → {v}: FORWARD EDGE")
                
                # Interval of u is entirely contained within interval of v
                elif self.discovery[v] < self.discovery[u] and self.finish[v] > self.finish[u]:
                    print(f"  {u} → {v}: BACK EDGE")
                
                # Intervals are disjoint (no ancestor/descendant relationship)
                else:
                    print(f"  {u} → {v}: CROSS EDGE")

# --- Test Environment ---
g = Graph()

# Main component
g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('B', 'C')
g.add_edge('D', 'E')
g.add_edge('C', 'E') # This will be a Cross Edge

# Let's add a forward edge to test that logic too
g.add_edge('A', 'C') 

# Disconnected component (to prove the fix works)
g.add_edge('X', 'Y')
g.add_edge('Y', 'Z')
g.add_edge('Z', 'X') # This will be a Back Edge

g.dfs('A')