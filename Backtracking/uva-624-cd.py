## replace this comment with how to calculate time complexity of backtracking problem


## can place function
def place(li, current_index, current_list, N):
    if current_index in list(current_list.keys()) or sum(list(current_list.values()))+li[current_index]>N:
        return False
    return True
def backtrack(li, N, no_of_tracks, current_list={}, ans=[]):
    # exit condition
    if not ans or abs(sum(ans)-N)> abs(sum(list(current_list.values()))-N):
        ans = list(current_list.values())
    # recurrence
    for i in range(no_of_tracks):
        # import pdb;pdb.set_trace()
        if place(li, i, current_list,N):
            current_list[i]=li[i]
            ans = backtrack(li, N, no_of_tracks, current_list, ans)
            current_list.pop(i)
    
    return ans


while True:
    li = list(map(int, input().split(" ")))
    ans = []
    N=li[0]
    no_of_tracks=li[1]
    li=li[2:]
    print(backtrack(li, N, no_of_tracks, {}, ans))

