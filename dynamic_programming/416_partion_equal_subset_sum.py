class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums)%2!=0:
            return False
        
        target=int(sum(nums)/2)
        dp=[[0 for i in range(target+1)] for j in range(len(nums)+1)]
        # print(dp)
        for row in range(1, len(nums)+1):
            for col in range(1, target+1):
              dp[row][col]=dp[row-1][col]
              
              if col>=nums[row-1] and dp[row-1][col-nums[row-1]]+nums[row-1]>dp[row][col]:
                  dp[row][col]=dp[row-1][col-nums[row-1]]+nums[row-1]
        
        ## code to find selected elements
        # i=len(nums)
        # col=target
        # selected_items=[]
        # while i>0 and col>0:
    
        #     if dp[i][col]==dp[i-1][col]:
        #         i-=1
        #     else:
        #         selected_items.append(nums[i-1])
        #         col-=nums[i-1]
        #         i-=1
        # import pdb;pdb.set_trace()
        if dp[len(nums)][target]==target:
            return True
        else:
            return False
                

        # pass


s=Solution()
nums = [1,5,11,5]
s.canPartition(nums)