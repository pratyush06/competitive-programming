import math
import re
import copy
class Solution:

    def search(self, nums: list[int], target: int, orign_nums:list[int]) -> int:
        mid_ele=math.floor(len(nums)/2)
        if mid_ele==0 and nums[mid_ele]!=target:
            return -1
        elif mid_ele==0 and nums[mid_ele]==target:
            return orign_nums.index(target)
        elif nums[mid_ele-1]<target:
           return self.search(nums[mid_ele:], target, orign_nums)
        elif nums[mid_ele-1]>target:
            return self.search(nums[:mid_ele], target, orign_nums)
        
        elif nums[mid_ele-1]==target:
            return orign_nums.index(target)
        
        
        
s= Solution()
print(s.search([-1,0,3,5,9,12], 9, [-1,0,3,5,9,12]))