#given list find all permutation of that list ex:-[1,2]==[[1,2],[2,1]]
import math

class Solution:
    def find(self, orignal, sol=[]):
        if len(sol)==len(orignal):
            final_sol.append(sol.copy())
            return
        
        for curr in orignal:
            # import pdb;pdb.set_trace()
            if curr in sol:
                continue
            sol.append(curr)
            self.find(orignal, sol)
            sol.pop()


s=Solution()
final_sol=[]
s.find([1,2])
print(final_sol)

        
