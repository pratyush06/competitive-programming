# coin change find no of ways
# to handle test case with value 0 start column search from oth colum
class Solution:
    def findTargetSumWays(self, nums, target) -> int:
        import pdb;pdb.set_trace()
        # nums.sort(reverse=True)
        # new_target=(sum(nums)+target)//2
        # if new_target%2!=0:
        #     return 0
        
        if((sum(nums)+target)%2==1 or abs(target)>sum(nums)):
            return 0
        
        new_target = (sum(nums) + target)//2
        
        dp=[[0 for i in range(new_target+1)] for j in range(len(nums)+1)]
        # no_of_ways=0
        for i in range(len(nums)+1):
            dp[i][0]=1
        for row in range(1, len(nums)+1):
            for col in range(0, new_target+1):
                # dp[row][col]=dp[row-1][col]
                # if col>=nums[row-1] and dp[row-1][col-nums[row-1]]+nums[row-1]>dp[row][col]:
                #     dp[row][col]=dp[row-1][col-nums[row-1]]+nums[row-1]
                # if dp[row][col]==new_target:
                #     no_of_ways+=1
                
                # import pdb;pdb.set_trace()
                
                if nums[row-1]<=col:
                    dp[row][col]=dp[row-1][col]+dp[row-1][col-nums[row-1]]
                
                else:
                    dp[row][col]=dp[row-1][col]
        
        
        return dp[len(nums)][new_target]
        # print(dp)

s=Solution()
# nums = [1, 1, 1, 1, 1]
# nums=[1] 
nums=[0,0,0,0,0,0,0,0,1]
# nums=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
target = 1
print(s.findTargetSumWays(nums, target))
# [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]