"""
Backtracking time = explored states * work per state; model recursion as a search tree with depth d (number of decisions) and branching b (max choices per step), so worst-case states ≈ O(b^d) or, when choices shrink like permutations, about O(n!); then multiply by the per-node work for safety checks or updates, and if enumerating all solutions include output-size costs (e.g., subsets need O(2^n* n) to print); quick heuristics: n steps with k choices each ⇒ O(k^n), choose among remaining each step ⇒ O(n!), include/exclude per item ⇒ O(2^n), and listing outputs costs at least linear in total outputs; space is usually call stack O(d) plus any bookkeeping like visited/diagonals O(n), and storing all solutions scales with output size.
"""

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

