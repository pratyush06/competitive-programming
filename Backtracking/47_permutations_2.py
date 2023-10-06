from typing import List

class Solution:
    def place(self, pos, index):
        if pos not in index:
            return True
        return False
        
    def permuteUnique(self, nums: List[int], curr=[], index=[], ans=None) -> List[List[int]]:
        if ans is None:
            ans=[]
        if len(curr)==len(nums) and curr not in ans:
            ans.append(curr.copy())
            return ans
        for i in range(len(nums)):
            if self.place(i, index):
                index.append(i)
                curr.append(nums[i])
                self.permuteUnique(nums, curr, index, ans)
                index.pop()
                curr.pop()
        return ans
s=Solution()
print(s.permuteUnique([1,1,2]))