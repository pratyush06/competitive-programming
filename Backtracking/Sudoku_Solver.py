class Solution:
    def solveSudoku(self,  board: list[list[str]]) -> None:

        def place(curr_row, curr_col, curr_num):
            vertical_board=list(zip(*board))
            if str(curr_num) in board[curr_row] or str(curr_num) in vertical_board[curr_col]:
                return False
            return True

        ans=False
        def backtrack(curr_row, curr_col):
            nonlocal ans
            if curr_row ==len(board):
                # import pdb;pdb.set_trace()
                ans=True
                print(board)
                return
            
            if curr_col==len(board):
                backtrack(curr_row+1, 0)
                return
            
            if (board[curr_row][curr_col]=='.') and (not ans):
                for curr_num in range(1, 10):
                    # import pdb;pdb.set_trace()
                    if place(curr_row,curr_col, curr_num):
                        board[curr_row][curr_col]=str(curr_num)
                        
                        backtrack(curr_row, curr_col+1)
                        board[curr_row][curr_col]='.'
            

                        
            
            elif not ans:
                backtrack(curr_row, curr_col+1)

        backtrack(0,0)
        



s=Solution()
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)

ans=[['5', '3', '1', '2', '7', '6', '4', '9', '8'],
     ['6', '2', '3', '1', '9', '5', '8', '4', '7'],
     ['1', '9', '8', '3', '4', '7', '5', '6', '2'],
     ['8', '1', '2', '7', '6', '4', '9', '5', '3'],
     ['4', '7', '9', '8', '5', '3', '6', '2', '1'],
     ['7', '4', '5', '9', '2', '8', '3', '1', '6'],
     ['9', '6', '7', '5', '3', '1', '2', '8', '4'],
     ['2', '8', '6', '4', '1', '9', '7', '3', '5'],
     ['3', '5', '4', '6', '8', '2', '1', '7', '9']]


# TLE Error for this solution
