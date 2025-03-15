import copy
class Solution:
    def place(self, target, curr_sol,final, curr_ele):
        if sum(curr_sol)<target:
            return True
        
        return False
    
    def combinationSum(self, candidates, target: int, curr_sol=None, final=None):
        if curr_sol is None:
            curr_sol=[]
        if final is None:
            final=[]
        if sum(curr_sol)==target:
            intermediate=sorted(curr_sol)
            flag=False
            if intermediate in final:
                flag=True
            if not flag:
                final.append(intermediate)
            return
        for i in candidates:
            if self.place(target, curr_sol, final, i):
                curr_sol.append(i)
                self.combinationSum(candidates, target, curr_sol, final)
                curr_sol.pop()
        
        return final
        


s=Solution()
# candidates = [2,3,6,7]
# target = 7

# candidates = [2,3,5]
# target = 8
candidates=[36,21,2,3,23,24,38,22,11,14,15,25,32,19,35,26,31,13,34,29,12,37,17,20,39,30,40,28,27,33]
target=35
# candidates = [2]
# target = 1
print(s.combinationSum(candidates, target))

## find which items are picked

i=n
while i>0 and j>0:
    
    if dp[i][j]==dp[i-1][j]:
        i-=1
    else:
        j-=weight[i]
        i-=1