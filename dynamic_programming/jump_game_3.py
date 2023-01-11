#solution worked but got TLE

class Solution:
    def canReach(self, arr, start, visited=None, ans=False):
        # import pdb;pdb.set_trace()

        if start>=len(arr) or start<0 or ans:
            return ans
        
        if visited is None:
            visited=[]
            # visited.append(start)
        if arr[start]==0:
            ans=True
            
        if len(visited)==len(arr)-1:
            return ans
        
        if (start not in visited):
            visited.append(start)
            ans=self.canReach(arr, start+arr[start], visited, ans)
            ans=self.canReach(arr, start-arr[start], visited, ans)
        return ans



# arr=[58,48,64,36,19,19,67,13,32,2,59,50,29,68,50,0,69,31,54,20,22,43,30,9,68,71,20,22,48,74,2,65,27,54,30,5,66,24,64,68,9,31,50,59,15,72,6,49,11,71,12,61,5,66,30,1,2,39,59,35,53,21,76,17,71,40,68,57,64,53,70,21,50,49,25,63,35]
arr=[4,2,3,0,3,1,2]
# arr=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
start=5
s=Solution()
print(s.canReach(arr, start))