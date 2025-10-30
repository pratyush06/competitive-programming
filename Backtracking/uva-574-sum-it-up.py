# iterating over entire list for all the backtracking function is too slow, different approch would be to use start pointer so we don't process same idx twice e.g is of this is given below
def place(idx, curr, total, numbers):
    if (numbers[idx]+sum(curr.values()))>total:
        return False
    return True



def backtrack(total, length, numbers, start, curr=None, ans=None):
    if curr is None:
        curr = {}
    if ans is None:
        ans = []
    # exit condition
    if sum(curr.values())==total:
        # import pdb;pdb.set_trace()
        if sorted(list(curr.values()), reverse=True) not in ans:
            ans.append(sorted(list(curr.values()), reverse=True))

    for i in range(start, len(numbers)):
        if place(i, curr, total, numbers):
            curr[i]=numbers[i]
            ans=backtrack(total, length, numbers, i+1, curr, ans)
            del curr[i]

    return ans



numbers = list(map(int, input().split(" ")))
total, length, numbers = numbers[0], numbers[1], numbers[2:]
answers = backtrack(total, length, numbers, 0)
print(answers)
# 400 12 50 50 50 50 50 50 25 25 25 25 25 25