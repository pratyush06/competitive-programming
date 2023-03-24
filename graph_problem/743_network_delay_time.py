#Dijkistra's algorithm

import collections
import heapq
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        edges=collections.defaultdict(list)
        for source, dist, weight in times:
            edges[source].append((dist,weight))

        import pdb;pdb.set_trace()
            
        minHeap=[(0, k)]
        visit=set()
        t=0
        while minHeap:
            sub_weight, sub_node=heapq.heappop(minHeap)
            if sub_node in visit:
                continue
            visit.add(sub_node)
            t=max(t, sub_weight)
            
            for adj_node, adj_weight in edges[sub_node]:
                if adj_node not in visit:
                    heapq.heappush(minHeap, (sub_weight+adj_weight, adj_node))
        return t if len(visit)==n else -1
    


s=Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,4,5],[3,4,1], [1,2,1],[2,3,1]], n=4, k=2))


