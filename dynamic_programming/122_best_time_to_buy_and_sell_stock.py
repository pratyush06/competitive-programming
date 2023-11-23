from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[None for _ in prices]
        profit=0
        dp[0]=prices[0]
        for i in range(1,len(prices)):
            if dp[i-1]>prices[i]:
                dp[i]=prices[i]
            if dp[i]==None:
                dp[i]=dp[i-1]
        return dp


s=Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))