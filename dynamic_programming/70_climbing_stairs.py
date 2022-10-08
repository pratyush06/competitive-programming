class Solution:
    def climbStairs(self, value: int, initialized_dp=False, dp=[]) -> int:
        if value==0:
            return dp[value]
        if not initialized_dp:
            dp=[0]*(value+1)
            dp[0]=1
            dp[1]=1
            # print(dp)
            initialized_dp=True
        
        if dp[value]!=0:
            return dp[value]
        
        else:
            dp[value-1]=self.climbStairs(value-1, initialized_dp, dp)
            dp[value-2]=self.climbStairs(value-2, initialized_dp, dp)
            dp[value]=dp[value-1]+dp[value-2]
            return dp[value]
        



        





s= Solution()
print(s.climbStairs(4))