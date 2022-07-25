class Solution:
    def generateParenthesis(self, n: int) -> list[str]:


        res=[]
        stack=[]

        def backtrack(openN, closeN):
            # import pdb;pdb.set_trace()

            if openN==closeN==n:
                res.append("".join(stack))
                return
            
            if openN<n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            
            if closeN<openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()

        
        backtrack(0,0)
        return res


s=Solution()
print(s.generateParenthesis(3))