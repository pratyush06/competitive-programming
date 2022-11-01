class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal=len(nums)-1
        import pdb;pdb.set_trace()
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False



s=Solution()
print(s.canJump([2,3,1,1,4]))