"""
Union-Find Time Complexity Comparison
====================================

1. Slow Union-Find (No Optimizations):
   - FIND: O(n) worst-case (e.g., skewed tree).
   - UNION: O(n) worst-case (due to unoptimized FIND).
   - Use case: Never in practice—too slow for large datasets.

2. Fast Union-Find (Union-by-Size + Path Compression):
   - FIND: O(α(n)) amortized (near-constant time).
   - UNION: O(α(n)) amortized (uses FIND internally).
   - α(n) = Inverse Ackermann function (effectively ≤ 4 for all practical n).
   - Use case: Always preferred (Kruskal’s MST, connected components, etc.).

Key Optimizations:
   - Union-by-Size: Attach smaller tree to larger tree (keeps depth ~log n).
   - Path Compression: Flattens tree during FIND for future speedups.

Example:
   - With 1 million elements:
     - Slow: O(n) → 1,000,000 steps per operation.
     - Fast: O(α(n)) → ~4 steps per operation.
"""

# Implementation Note: Always use Fast Union-Find!

#  Fast UNION Implementation (Slow FIND)
class DisjointSetSlowFind:
    def __init__(self, n):
        self.make_set(n)
    def make_set(self, n):
        self.s = [x for x in range(n)]
    
    def find (self, x):
        if S[x]==x:
            return x
        else:
            return self.find(x)
    
    def union(self, root1, root2):
        S[root1]=root2


# Fast Union Implementation (Qick Find) - by size

class DisjointSetQuickFindBySize:
    def __init__(self, n):
        self.make_set(n)  # Initialize the sets when creating the object
    
    def make_set(self, n):
        self.s = [-1 for x in range(n)]  # Each element is its own root initially
    
    def find(self, x):
        if self.s[x] < 0:
            return x
        else:
            # Path compression: flatten the structure for future finds
            self.s[x] = self.find(self.s[x])
            return self.s[x]
    
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return  # Already in the same set
        
        # Union by rank (using negative size for rank)
        if self.s[root2] < self.s[root1]:  # root2 has higher rank
            self.s[root2] += self.s[root1]
            self.s[root1] = root2
        else:
            self.s[root1] += self.s[root2]
            self.s[root2] = root1