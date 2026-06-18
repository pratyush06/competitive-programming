"""
Pattern: Dynamic programming for LIS
Recognition cue: Need longest increasing subsequence, not necessarily contiguous.
Key idea: dp[i] is the best LIS ending at i.
Time: O(n^2)
Space: O(n)
Common traps: Confusing subsequence with substring and using <= instead of <.
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1 for i in nums]
        for i in range(1, len(nums)):
            selected_items=[dp[j] for j in range(i) if nums[j]<nums[i]]
            dp[i]=1+max(selected_items, default=0)
        
        return max(dp)


s=Solution()
s.lengthOfLIS([10,9,2,5,3,7,101,18])
