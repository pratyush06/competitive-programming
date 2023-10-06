#find number of ways we can place 8 queen in chessboard


class Solution:
    def place(self, rows, r):
        if r in rows:
            return False
        else:
            for i in range(len(rows)):
                if abs(r-rows[i]) == abs(len(rows)-i):
                    return False    
        return True
    def backtrack(self, rows_and_cols, rows):
        if len(rows)==rows_and_cols:
            final_sol.append(rows.copy())
            return
        for r in range(rows_and_cols):
            if self.place(rows, r):
                rows.append(r)
                self.backtrack(rows_and_cols, rows)
                rows.pop()




s=Solution()

rows_and_cols=int(input('please enter size of chessboard: '))
rows=[]
final_sol=[]
s.backtrack(rows_and_cols, rows)
print(final_sol)



