class Solution:
    def maxArea(self, height) -> int:
        left, right=0, len(height)-1
        max=None
        while left < right:
            area=(right-left)*min(height[left], height[right])
            if max is None or max< area:
                max=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max
    

height = [1,8,6,2,5,4,8,3,7]
# height=[1,1]
s=Solution()
print(s.maxArea(height))