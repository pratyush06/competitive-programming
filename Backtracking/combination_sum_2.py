class Solution:
    
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        res=[]
        def dfs(i, curr, total):
            if total==target:
                if curr not in res:
                    res.append(curr.copy())   
                    return
            if i>=len(candidates) or total>target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()
            # print(res)
            dfs(i+1, curr, total)
            return res
        return dfs(0, [], 0)
s=Solution()
candidates = [2,5,2,1,2]
# candidates = [10,1,2,7,6,1,5]
# target = 8
candidates.sort()
target = 5
print(s.combinationSum2(candidates, target))