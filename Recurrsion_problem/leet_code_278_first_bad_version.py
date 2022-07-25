class Solution:
    def firstBadVersion(self, n:int, low=1) ->int:
        # import pdb;pdb.set_trace()
        mid=(low+n)//2
        if isBadVersion(mid) is False:
            return self.firstBadVersion(low=mid+1, n=n)
        
        elif isBadVersion(mid) is True and isBadVersion(mid-1) is False:
            return mid
        
        elif isBadVersion(mid) is True:
            return self.firstBadVersion(mid-1, low)
        
    




def isBadVersion(n:int)->bool:
    if n >= 1702766719:
        return True
    return False

s= Solution()
print(s.firstBadVersion(2126753390))