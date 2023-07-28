class Solution:    
    def isValid(self, si:str, res=None, flag=False):
        # import pdb;pdb.set_trace()
        if res is None:
            res=[]
        if flag:
            return not flag
        
        if len(si)==0:
            if len(res)==0:
                return True
            return False

        if len(si)==1 and len(res)==0:
            return False
        
        if si[0] in ('(', '{', '['):
            res.append(si[0])
        
        else:
            if len(res)>0:
                if (res[-1]=='(' and si[0]==')') or (res[-1]=='{' and si[0]=='}') or(res[-1]=='[' and si[0]==']'):
                    res.pop()
                else:
                    flag=True
            
            else:
                flag=True
            
        return self.isValid(si[1:], res, flag)
        
        
        
        
        
            



s ="((("
# (res[-1]=='(' and si[pos]==')') or (res[-1]=='{' and si[pos]=='}') or(res[-1]=='[' and si[pos]==']'):

sol=Solution()
print(sol.isValid(s))