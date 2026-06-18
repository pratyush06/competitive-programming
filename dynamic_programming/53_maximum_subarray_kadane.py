"""
Pattern: Kadane's algorithm
Recognition cue: Need maximum sum over a contiguous subarray.
Key idea: Best subarray ending at i either extends the previous one or starts at i.
Time: O(n)
Space: O(n) in this DP version, O(1) if keeping only previous best.
Common traps: Returning 0 for all-negative arrays.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]    
        for i in range(1, len(nums)):
            dp[i]=max(dp[i-1]+nums[i], nums[i])
        
        return max(dp)


s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
