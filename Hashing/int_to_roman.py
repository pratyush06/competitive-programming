class Solution:
    def intToRoman(self, num: int) -> str:
        rom_num_pair={'1':'I', '4':'IV', '5':'V','9':'IX', '10':'X', '40':'XL', '50':'L',
         '90':'XC', '100':'C', '400':'CD', '500':'D', '900':'CM', '1000':'M'}
        # import pdb;pdb.set_trace()

        ans=''

        for key in reversed(rom_num_pair.keys()):
    
            count=num // int(key)
            ans += (rom_num_pair[key]*count)
            num = num %int(key)
        
        # import pdb;pdb.set_trace()


        return ans



s=Solution()
print(s.intToRoman(58))