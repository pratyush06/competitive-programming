class Solution:
    def searchInsert(self, nums: list[int], target: int, first_time=True, orign_nums=None) -> int:
        # import pdb;pdb.set_trace()
        if first_time:
            orign_nums=nums.copy()
        mid=len(nums)//2
        if len(nums)==1:
            if nums[0]>target:
                return orign_nums.index(nums[0])
            else:
                return orign_nums.index(nums[0])
        elif nums[mid]<target:
            return self.searchInsert(nums[mid+1:], target, False, orign_nums)
        elif nums[mid]>target:
            return self.searchInsert(nums[:mid], target, False, orign_nums)
        
        elif nums[mid]==target:
            return orign_nums.index(target)



s=Solution()
print(s.searchInsert([1,3,5,6], 15))