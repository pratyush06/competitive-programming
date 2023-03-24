#DFS
class Solution:
    def numIslands(self, grid) -> int:
        counter=0
        import pdb;pdb.set_trace()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # print(grid[row][col])
                if(grid[row][col]!='0'):
                    counter+=1
                    self.dfs(row,col)
        return counter
                
                
    def dfs(self, row, col):
        if (row<0 or col<0 or row>=len(grid) or col>=len(grid[row]) or grid[row][col]=='0'):
            return
        grid[row][col]='0'
        self.dfs(row, col-1)
        self.dfs(row, col+1)
        self.dfs(row+1, col)
        self.dfs(row-1,col)
        
            
s=Solution()

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))
        