class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # print(len(grid[0]))
        dp=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
        # import pdb;pdb.set_trace()

        dp[0][0]=grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        
        for j in range(1, len(grid[0])):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        
        # print(dp)

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                # import pdb;pdb.set_trace()
                dp[row][col]=grid[row][col]+min(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]
        


# grid = [[1,3,1],[1,5,1],[4,2,1]]
grid=[[1,2,3],[4,5,6]]

s=Solution()
print(s.minPathSum(grid))