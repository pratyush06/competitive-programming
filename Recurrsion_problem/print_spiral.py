from typing import List
def printSpiral(arr:List):
    m=len(arr)
    n=len(arr[0])
    move = [(0,1), (1,0), (0,-1), (-1,0)]
    remains=m*n
    i=0
    j=0
    counter=0
    ans=[]
    while remains>0:
        ans.append(arr[i][j])
        arr[i][j]=None
        remains-=1
        for _ in range(len(move)):
            dx, dy=move[counter]
            new_i = i+dx
            new_j = j+dy
            if 0<=new_i<m and 0<=new_j<n and arr[new_i][new_j] is not None:
                i=new_i
                j=new_j
                break
            else:
                counter = (counter+1)%len(move)
    return ans

que=[[1,2,3, 4],
     [1,2,3, 4],
     [1,2,3, 4],
     [1,2,3, 4],
     [1,2,3, 4],
     [1,2,3, 4],
     [1,2,3, 4],
     [10,11,12, 11]]
print(printSpiral(que))


        