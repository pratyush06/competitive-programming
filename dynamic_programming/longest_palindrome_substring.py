class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal_str = ''
        for i in range(len(s)):
            import pdb;pdb.set_trace()
            left = i
            right = i
            while not (left < 0) and right < len(s) and s[left] == s[right]:
                if len(s[left:right + 1]) > len(pal_str):
                    pal_str = s[left:right + 1]
                left -= 1
                right += 1

            left = i
            right = i+1
            while not (left < 0) and right < len(s) and s[left] == s[right]:
                if len(s[left:right + 1]) > len(pal_str):
                    pal_str = s[left:right + 1]
                left -= 1
                right += 1

        return pal_str


s = Solution()
print(s.longestPalindrome('abb'))