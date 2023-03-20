class Solution:
    def maxProfit(self, prices) -> int:
        # import pdb;pdb.set_trace()
        profit=0
        dp=[None for i in range(len(prices))]
        dp[0]=prices[0]
        
        for i in range(1, len(prices)):
            if dp[i-1]>prices[i]:
                dp[i]=prices[i]
            
            if dp[i]==None:
                dp[i]=dp[i-1]
                
            if (prices[i]-dp[i-1])>profit:
                profit=prices[i]-dp[i-1]
            
        return profit


s=Solution()
# prices = [7,1,5,3,6,4]
prices=[2,1,2,1,0,1,2]
print(s.maxProfit(prices))