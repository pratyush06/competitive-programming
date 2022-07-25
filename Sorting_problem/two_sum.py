from itertools import combinations
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # import pdb;pdb.set_trace()
        seen={}
        for i,num in enumerate(nums):
            if target-num in seen:
                return([seen[target-num],i])
            elif num not in seen:
                seen[num]=i


s=Solution()
nums = [2,7,11,15] 
target = 9
print(s.twoSum(nums, target))