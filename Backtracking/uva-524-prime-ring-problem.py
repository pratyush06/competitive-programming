# we can further reduce time complexity by calculating which all are prime number's till sum of n before hand using sieve of eratosthenes algorithm
# which will elemenate all the for loop we have inside place function further improving time complexity
import copy
def place(idx, curr, n):
    if idx in curr:
        return False
    
    second_last = curr[-1]
    summation = second_last+idx
    for i in range(2, summation):
        if summation%i==0:
            return False
    if len(curr)==n-1:
        # import pdb;pdb.set_trace()
        summation = idx+1
        for i in range(2, summation):
            if summation%i==0:
                return False
    return True



def backtrack(n, curr=None, ans=None):
    if curr is None:
        curr=[1,]
    if ans is None:
        ans=[]
    if len(curr)==n:
        # import pdb;pdb.set_trace()
        ans.append(copy.copy(curr))
    # exit condition

    # import pdb;pdb.set_trace()
    for i in range(2,n+1):
        if place(i, curr, n):
            curr.append(i)
            ans = backtrack(n, curr, ans)
            # print(curr)
            curr.pop()

    return ans



n = int(input())
print(backtrack(n))