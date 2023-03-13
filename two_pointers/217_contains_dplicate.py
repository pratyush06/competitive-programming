class Solution:
    def containsDuplicate(self, nums) -> bool:
        # import pdb;pdb.set_trace()
        # nums.sort()
        nums=self.quickSort(nums)
        import pdb;pdb.set_trace()
        hasDplicate=False
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                hasDplicate=True
                break
        return hasDplicate
    
    def quickSort(self, nums):
        if len(nums)<=1:
            return nums
        # import pdb;pdb.set_trace()
        pivot=nums[0]
        left=[]
        right=[]
        equal=[]
        
        for j in nums:
            if j<pivot:
                left.append(j)
            if j>pivot:
                right.append(j)
            else:
                equal.append(j)
        return self.quickSort(left)+equal+self.quickSort(right)

s=Solution()
print(s.containsDuplicate(nums = [1, 2,3,4,1]))