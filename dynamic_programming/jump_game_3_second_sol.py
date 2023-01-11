import collections
class Solution:
    def canReach(self, arr, start):
        q=collections.deque()
        cache=set()
        q.append(start)
        
        while q:
            index=q.popleft()
            if arr[index]==0:
                return True
            # import pdb;pdb.set_trace()
            for x in ((index+arr[index]),(index-arr[index])):
                if 0<=x<len(arr) and x not in cache:
                    q.append(x)
                    cache.add(index)
        
        return False
    


s=Solution()

arr=[4,2,3,0,3,1,2]
start=5
print(s.canReach(arr, start))

        