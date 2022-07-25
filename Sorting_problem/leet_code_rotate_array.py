class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        nums.reverse()
        print(nums)
        temp=nums[-k:]
        nums=nums[:-k]
        nums=temp+nums
        # print(nums)
        # nums.remove(temp)
        # print(nums)
        # result=[]
        # result=list(filter(lambda i:i not in temp, nums))
        # print(result)

s=Solution()
s.rotate([1,2,3,4,5,6,7],3)