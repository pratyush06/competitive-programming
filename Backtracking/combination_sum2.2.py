class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        res=[]
        
        def backtrack(curr, pos, target):
            # import pdb;pdb.set_trace()
            if target==0:
                res.append(curr.copy())
                return
            if target<=0:
                return
            prev=-1
            for i in range(pos, len(candidates)):
                if candidates[i]==prev:
                    continue
                curr.append(candidates[i])
                backtrack(curr, i+1, target-candidates[i])
                curr.pop()
                prev=candidates[i]
            
        backtrack([], 0, target)
        return res
    



s=Solution()
candidates = [2,5,3,4]
target=5
print(s.combinationSum2(candidates, target))