class Solution:
    def permute(self, nums, sol=None, final_sol=None):
        if sol is None:
            sol=[]
        if final_sol is None:
            final_sol=[]
        if len(sol)==len(nums):
            final_sol.append(sol.copy())
            return
        
        for curr in nums:
            if curr in sol:
                continue
            sol.append(curr)
            self.permute(nums, sol, final_sol)
            sol.pop()
    
        # import pdb;pdb.set_trace()
        return final_sol


s=Solution()
nums=[1,2,3]
print(s.permute(nums))