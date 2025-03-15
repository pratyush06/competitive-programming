### solution works but got TLE error

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp=[0]*len(nums)
        return self.backtrack(0, dp, nums, False)

    def backtrack(self, curr_index, dp, nums, ans=False):
        # import pdb;pdb.set_trace()
        if len(nums)-1==sum(dp):
            ans=True
            return True
            
        elif self.place(nums=nums, dp=dp, curr_index=curr_index):
            for i in range(nums[curr_index], 0, -1):
                if ans:
                    break
                dp[curr_index]=i
                ans = self.backtrack(curr_index=sum(dp), dp=dp, nums=nums, ans=ans)
                dp[curr_index]=0
        
        return ans

    
    def place(self, nums, dp, curr_index):
        if sum(dp)>=len(nums) or nums[curr_index]==0:
            return False
        
        return True



s=Solution()
print(s.canJump([0,0,0]))