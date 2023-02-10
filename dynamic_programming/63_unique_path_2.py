class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # import pdb;pdb.set_trace()
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        # import pdb;pdb.set_trace()
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        # import pdb;pdb.set_trace()
        for i in range(col):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i]=1
        # import pdb;pdb.set_trace()
        
        for j in range(row):
            # import pdb;pdb.set_trace()
            if obstacleGrid[j][0]==1:
                break
            dp[j][0]=1
        # import pdb;pdb.set_trace()
        for i in range(1, row):
            for j in range(1,col):
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[row-1][col-1]

s=Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))