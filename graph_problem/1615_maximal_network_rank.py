import collections
import queue
class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        dp=[[None for i in range(n)] for i in range(n)]
        edges=collections.defaultdict(list)
        unvisited=queue.Queue()
        rank={}
        visit=set()
        
        
        for i in range(n):
            unvisited.put(i)
            rank[i]=0
            
        for source, dist in roads:
            edges[source].append((dist, 1))
            edges[dist].append((source, 1))
            dp[source][dist]=0
            dp[dist][source]=0
            # unvisited.put(source)
            # unvisited.put(dist)
            # rank[source]=0
            # rank[dist]=0
        
        
        while not unvisited.empty():
            # import pdb;pdb.set_trace()
            node=unvisited.get()
            if node in visit:
                continue
            visit.add(node)
            for next_node, next_weight in edges[node]:
                if next_node not in visit:
                    continue
                rank[node]+=next_weight
                rank[next_node]+=next_weight
        
        if len(rank)==0:
            return 0
        max=None
        for row in range(len(dp)):
            for col in range(len(dp[row])):
                # import pdb;pdb.set_trace()
                if row==col:
                    continue
                elif dp[row][col]==None:
                    dp[row][col]=rank[row]+rank[col]
                else:
                    dp[row][col]=(rank[row]+rank[col])-1
                if max==None or dp[row][col]>max:
                    max=dp[row][col]
        
        # import pdb;pdb.set_trace()
        return max
            
                
                
                    
                
                    
        # import pdb;pdb.set_trace()
        
        # max=None
        # for row in roads:
        #     if max is None or max<(rank[row[0]]+rank[row[1]]):
        #         max=(rank[row[0]]+rank[row[1]])
        
        # return max
            
        
    

s=Solution()
roads = [[0,1],[0,3],[1,2],[1,3]]
# roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
n=4
# roads=[]

print(s.maximalNetworkRank(n,roads))