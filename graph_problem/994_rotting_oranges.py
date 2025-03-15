import queue
class Solution:
    def orangesRotting(self, grid) -> int:
        L=queue.Queue()
        dist_mat=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]==2:
                    dist_mat[row][col]=0
                    L.put((row, col))
                if grid[row][col]==0:
                    dist_mat[row][col]=-1
                    
                    
        dx=(-1, 1,0,0)
        dy=(0,0,-1,1)
        while not L.empty():
            node=L.get()
            for i in zip(dx, dy):
                x1=node[0]+i[0]
                y1=node[1]+i[1]
                
                if(x1<0 or y1<0 or x1 >=len(grid) or y1 >=len(grid[x1]) or grid[x1][y1]==0 or grid[x1][y1]==2):
                    continue
                
                grid[x1][y1]=2
                L.put((x1, y1))
                dist_mat[x1][y1]=dist_mat[node[0]][node[1]]+1
        
        # import pdb;pdb.set_trace()
        
        max_ele=0
        for row in zip(grid, dist_mat):
            if max_ele==-1:
                break
            for ele in zip(row[0], row[1]):
                # import pdb;pdb.set_trace()
                if ele[0]==1:
                    max_ele=-1
                    break
                if max_ele is None or max_ele<ele[1]:
                    # import pdb;pdb.set_trace()
                    max_ele=ele[1]
        
        return max_ele
                
    

s=Solution()
# grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
print(s.orangesRotting(grid))