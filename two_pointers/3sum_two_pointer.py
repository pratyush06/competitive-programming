class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:continue
            ji=i+1
            k=len(nums)-1
            while(ji<k):
                # import pdb;pdb.set_trace()
                sum=nums[i]+nums[ji]+nums[k]
                if sum <0:
                    ji+=1
                elif sum>0:
                    k-=1
                else:
                    ans.append([nums[i], nums[ji], nums[k]])
                    ji+=1
                    k-=1
                    while ji<k and nums[ji]==nums[ji-1]:ji+=1
                    while ji<k  and nums[k]==nums[k+1]:k-=1
        return ans


s=Solution()
nums=[1,-1,-1,0]
print(s.threeSum(nums))