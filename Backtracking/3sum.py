# got TLE error
class Solution:
    def threeSum(self, nums):
        
        def place(curr, i):
            if len(curr)<=3 and i not in curr:
                return True
        
        def backtrack(nums, curr=None, final=None, curr_ele=None, pos=0):
            # base condition
            if sum(curr_ele)==0 and len(curr)==3:
                sorted_ele=sorted(curr_ele)
                if sorted_ele not in final:
                    final.append(sorted_ele.copy())
                    return
            for i in range(pos, len(nums)):
                if place(curr, i):
                    curr.append(i)
                    curr_ele.append(nums[i])
                    pos+=1
                    backtrack(nums, curr, final, curr_ele, pos)
                    curr.pop()
                    curr_ele.pop()
            return final
        
        return backtrack(nums, [], [], [])

s=Solution()
nums = [-1,0,1,2,-1,-4]
# nums=[1,-1,-1,0]
print(s.threeSum(nums))

        
        
                