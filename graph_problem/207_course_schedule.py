#topological sort

import queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        dp=[[None for i in range(numCourses)] for j in range(numCourses)]
        indegree={}
        
        for i in range(numCourses):
            indegree[i]=0
        for i in prerequisites:
            # import pdb;pdb.set_trace()
            dp[i[1]][i[0]]=1
            indegree[i[0]]+=1
        print(indegree)
#         for i in prerequisites:
# ...     indegree[i[0]]=1
        ans=0
        L=queue.Queue()
        
        for i in indegree.items():
            if i[1]==0:
                L.put(i[0])
                ans+=1
        # print
        while L.empty()!=True:
            element=L.get()
            # import pdb;pdb.set_trace()
            for i in range(len(dp[element])):
                if dp[element][i]==1:
                    indegree[i]-=1
                    if indegree[i]==0:
                        L.put(i)
                        ans+=1
        return ans==numCourses
                

s=Solution()
print(s.canFinish(2,[[0,1]]))