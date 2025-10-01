# --- [PYTHON PITFALL & SOLUTION] Mutable Default Arguments ---
#
# THE PROBLEM: A default argument like `my_list=[]` or `my_dict={}` is created
# only ONCE, when the function is first defined. This single object is then
# shared across ALL calls that use the default. Modifying it in one call
# will unexpectedly affect all future calls.
#
#   def buggy_func(item, my_list=[]):  # This list is SHARED!
#       my_list.append(item)
#       return my_list
#
#   # >>> buggy_func(1)
#   # [1]
#   # >>> buggy_func(2)  <-- Unexpectedly returns [1, 2]
#
# THE SOLUTION: The standard Python idiom is to use an immutable default like
# `None`. Inside the function, we check for `None` and create a NEW list or
# dict. This guarantees that every call that relies on the default gets its
# own fresh, independent object.
#
# This line below implements that correct and safe pattern.
# if current_pos is None:
#     current_pos = []


import copy

def place(curr_idx, current_pos):
    # import pdb;pdb.set_trace()
    if (curr_idx in current_pos):
        return False
    
    else:
        for i in range(len(current_pos)):
            if abs(curr_idx - current_pos[i]) == abs(len(current_pos) - i):
                return False
    return True

def backtrack(queen_pos, current_pos=[], ans=None, current_count=0):
    # print(f" length of current pos {current_pos}")
    if  len(current_pos)==8:
        # if current_count==8:
        #     import pdb;pdb.set_trace()
        if not ans or current_count<ans:
            ans=current_count
        # temp_ans = 0
        # for k, j in enumerate(queen_pos):
        #     if current_pos[k]!=k:
        #         temp_ans+=1
        
        # if not ans or temp_ans<ans:
        #     ans = temp_ans

    for i in range(1, 9):
        if place(i, current_pos):
            # if i==1 and current_pos==[2, 4, 6, 8, 3]:
            #     import pdb;pdb.set_trace()
            cost = 0
            if i!=queen_pos[len(current_pos)]:
                cost=1
            current_pos.append(i)
            ans=backtrack(queen_pos, current_pos, ans, current_count+cost)
            current_pos.pop()
            # current_count-=1
    return ans

case_no = 1
while True:
    queen_pos = list(input().split(" "))
    # import pdb;pdb.set_trace()
    if queen_pos[0]=="":
        break
    queen_pos = list(map(int, queen_pos))
    # queen_pos = [None]+queen_pos
    # queen_pos = [1, 2,3,4,5,6,7,8]
    new=backtrack(queen_pos)

    # import pdb;pdb.set_trace()
    print(f"Case {case_no}: {new}")
    case_no+=1
