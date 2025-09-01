# solution is not complete try to improve

from collections import Counter

class wakeupUnion:
    def __init__(self, no_of_vertex):

        self.s = [-1]*no_of_vertex
        self.connecton = [set() for _ in range(no_of_vertex)]
    
    def find(self, x):
        if self.s[x]<0:
            return x

        else:
            self.s[x] = self.find(self.s[x])
            return self.s[x]
    
    def union(self, x, y):
        self.connecton[x].add(y)
        self.connecton[y].add(x)
        root1 = self.find(x)
        root2 = self.find(y)
        if root1==root2:
            return
        if self.s[root1]<self.s[root2]:
            self.s[root1]+=self.s[root2]
            self.s[root2]=root1
        else:
            self.s[root2]+=self.s[root1]
            self.s[root1]=root2



no_of_slept_areas = int(input())
no_of_connection = int(input())
wakeup_area = tuple(input())
edges = []
char_to_idx = {}
count = 0
for _ in range(no_of_connection):
    edge = input()
    for i, char in enumerate(edge):
        if char not in char_to_idx.keys():
            char_to_idx[char]=count
            count+=1
    edges.append(tuple(edge))

for ch in wakeup_area:
    if ch not in char_to_idx.keys():
        char_to_idx[ch]=count
        count+=1

print(edges)
print(char_to_idx)
wu = wakeupUnion(len(char_to_idx.keys()))
for t in edges:
    wu.union(char_to_idx[t[0]], char_to_idx[t[1]])

print(f"relations {wu.connecton}")
print(f"serial {wu.s}")

def common_in_at_least_three(sets_list):
    if len(sets_list) < 3:
        return None
    
    # Count occurrences of each element across all sets
    counter = Counter()
    for s in sets_list:
        counter.update(s)
    
    # Return elements that appear in at least 3 sets
    return {element for element, count in counter.items() if count >= 3}
ans_list = []
wakeup_area_idx = set()
for w in wakeup_area:
    ans_list.append(wu.connecton[char_to_idx[w]])
    wakeup_area_idx.add(char_to_idx[w])
year = 0
while True:
    # import pdb;pdb.set_trace()
    year+=1
    result = common_in_at_least_three(ans_list)
    if not result:
        break
    union_of_all = set().union(*ans_list)
    remaining = result - union_of_all
    if not remaining:
        break
    for k in remaining:
        if k not in wakeup_area_idx:
            ans_list.append(wu.connecton[k]) 
            wakeup_area_idx.add(k)
    
    if len(wakeup_area_idx)==len(char_to_idx.keys()):
        break

print(f"year-----------{year}")