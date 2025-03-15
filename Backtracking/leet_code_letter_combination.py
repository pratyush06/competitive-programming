from functools import partial
from typing import final


class Solution:
    def letterCombinations(self, digits: str, current_digit=0, partial_sol='', final_sol=[]) -> list[str]:
        if current_digit==len(digits):
            final_sol.append(partial_sol)
            return
        x=list(digits)
        num_digit_mapping={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        current_letter=list(num_digit_mapping[x[current_digit]])
        # partial_sol=''
        for i in current_letter:
            # import pdb;pdb.set_trace()
            partial_sol+=i
            self.letterCombinations(digits=digits,current_digit=current_digit+1, partial_sol=partial_sol, final_sol=final_sol)
            partial_sol=partial_sol[:-1]
        
        return final_sol

        


s=Solution()
print(s.letterCombinations('2'))