class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i = int(m - 1)
        j = int(n - 1)
        k = int(m + n - 1)
        
        while (k >= 0):
            if i>=0 and j>=0:
                if(nums2[j] > nums1[i]):
                    nums1[k] = nums2[j]
                    k -= 1
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    k -= 1
                    i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                break
    
    
                

nums1 = [4,0,0,0,0,0] 
m = 1
nums2 = [1,2,3,5,6] 
n = 5
s=Solution()
print(s.merge(nums1,m, nums2, n))

