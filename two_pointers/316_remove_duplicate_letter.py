class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last={}
        vis={}
        ans=[]
        for idx, val in enumerate(s):
            last[val]=idx
        for idx, val in enumerate(s):
            if val in vis.keys() and vis[val]:
                continue
            while (len(ans)!=0 and ans[-1]>val and last[ans[-1]]>idx):
                vis[ans[-1]]=False
                ans.pop()
            
            ans.append(val)
            vis[val]=True
        
        return "".join(ans)
                      
    

s=Solution()
print(s.removeDuplicateLetters("cbacdcbc"))