class Solution:
    def longestValidParentheses(self, s:str)->int:
        max_len=0
        i=0
        left=0
        right=0
        while i<len(s):
           if s[i]=='(':
               left+=1
           else:
               right+=1
            
           if left==right:
               max_len = max(max_len, left+right)
               print(max_len)
           elif right>left:
               left=right=0
           i+=1
        
        i=len(s)-1
        left=right=0
        while i>=0:
            if s[i]=="(":
                left+=1
            else:
                right+=1
            
            if left==right:
                max_len=max(max_len, left+right)
            elif left>right:
                left=right=0
            i-=1
        return max_len
            

su=Solution()
print(su.longestValidParentheses("(())"))
