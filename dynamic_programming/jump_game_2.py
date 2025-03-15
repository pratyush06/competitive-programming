# got TLE 

class Solution:
    def jump(self, nums, curr_index=None, dp=None, final_sol=0) -> int:
        if curr_index==len(nums)-1:
            # import pdb;pdb.set_trace()
            print(dp)
            if final_sol == 0 or final_sol > sum(dp):
                final_sol=sum(dp)
            return final_sol
        
        if dp is None:
            dp=[0]*len(nums)
            # dp[0]=1
            curr_index=0

        for i in range(1, nums[curr_index]+1):
            # import pdb;pdb.set_trace()  
            if i+curr_index>len(nums)-1 or nums[curr_index]==None:
                continue
            dp[i+curr_index]=1
            # curr_index=i+curr_index
            final_sol=self.jump(nums, i+curr_index, dp, final_sol)
            dp[curr_index]=0
        
        return final_sol
        # print(dp)
            # for j in range(1, i[1]+1):
            #     dp[i[0]+j]=1
            #     pass
            # for j in range(1, i+1):



s=Solution()
print(s.jump([2,3,1,1,4]))