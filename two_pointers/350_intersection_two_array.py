class Solution:
    def intersect(self, nums1, nums2):
        # import pdb;pdb.set_trace()
        nums1.sort()
        nums2.sort()
        ans=[]
        i=0
        j=0
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j] and i<len(nums1):
                i+=1
            elif nums2[j]<nums1[i] and j<len(nums2):
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        
        return ans


# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,9] 
nums2 = [9,4,9,8,4]

s=Solution()
print(s.intersect(nums1, nums2))