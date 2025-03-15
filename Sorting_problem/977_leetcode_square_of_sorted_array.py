# try merge sort with quick sort got TLE error
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sq_nums=list(map(lambda x:x*x, nums))
        # return self.quickSort(sq_nums)
        return self.mergesort(sq_nums)
        


    def quickSort(self, nums:list[int])->list[int]:
        if len(nums)<=1:
            return nums
        
        pivot=nums[0]
        left=[]
        right=[]
        equal=[]
        for j in nums:
            if j<pivot:
                left.append(j)
            elif j>pivot:
                right.append(j)
            else:
                equal.append(j)
        
        return self.quickSort(left)+equal+self.quickSort(right)
    
    def mergesort(self, nums:list[int])->list[int]:
        list_length=len(nums)
        if list_length==1:
            return nums
        
        mid=list_length//2
        left_partition=self.mergesort(nums[:mid])
        right_partition=self.mergesort(nums[mid:])
        return self.merge_left_and_right(left_partition, right_partition)
    
    def merge_left_and_right(self, left, right):
        output=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                output.append(left[i])
                i+=1
            else:
                output.append(right[j])
                j+=1
        output.extend(left[i:])
        output.extend(right[j:])
        return output

s=Solution()
print(s.sortedSquares([-4,-2,0,1,2]))