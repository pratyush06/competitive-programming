## verdict is TLE but it seems vertices.index is a costly operation O(n) try using dictinory may result in accepted verdict
# but goal to learn union find is achived 

class ForestUnion:
    def __init__(self, vertices):
        self.s = [-1 for _ in range(len(vertices))]
    
    def find(self, x):
        if self.s[x]<0:
            return x
        else:
            self.s[x] = self.find(self.s[x])
            return self.s[x]
    def union(self, x, y):
        idx_x, idx_y = vertices.index(x), vertices.index(y)
        root1 = self.find(idx_x)
        root2 = self.find(idx_y)
        if root1==root2:
            return
        
        if self.s[root1]<self.s[root2]:
            self.s[root1]+=self.s[root2]
            self.s[root2]=root1
        else:
            self.s[root2]+=self.s[root1]
            self.s[root1]=root2


no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    total_edges = []
    vertices = []
    while True:
        edge = input()
        cleaned = edge.strip('()').split(',')
        result = tuple(x.strip() for x in cleaned)
        if "*" not in edge:
            total_edges.append(result)
        else:
            break
    vertices = list(input().split(','))
    fu = ForestUnion(vertices)
    for e in total_edges:
        fu.union(e[0], e[1])
    
    trees = [t for t in fu.s if t < 0 and t != -1]
    acorn =[ t for t in fu.s if t==-1]
    print(f"There are {len(trees)} tree(s) and {len(acorn)} acorn(s).")
    



