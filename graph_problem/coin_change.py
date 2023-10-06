from typing import List

def coinChange(arr:List):
    arr.sort()
    total=[]
    def dfs(i, curr):
        if sum(curr) not in total:
            total.append(sum(curr))
        if i>=len(arr):
            return
        curr.append(arr[i])
        dfs(i+1, curr)
            # print(res)
        curr.pop()
        dfs(i+1, curr)
        return total
    return dfs(0, [])


# ans=coinChange([1,1,5,2,3,7, 99])
# print(sorted(ans))


def newSolution(arr:List):
    count = 0
    for i in arr:
        if count + 1 >= i:
            count = count + i
        else:
            return count + 1
    return count + 1

que=[1,1,5,2,3,7, 99]
que.sort()
ans=newSolution(que)
print(ans)