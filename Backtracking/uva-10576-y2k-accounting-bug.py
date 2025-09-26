import copy
def place(curr_ele, current_list):
    if len(current_list)>=4 and (curr_ele+sum(current_list[-4:]))>0:
        return False
    
    return True

def bactrack(sd_list, ans=[], current_list=[]):
    if len(current_list)==12:
        if sum(ans)<sum(current_list):
            ans = copy.copy(current_list)
        return ans
    for j in sd_list:
        if place(j, current_list):
            current_list.append(j)
            ans = bactrack(sd_list, ans, current_list)
            current_list.pop()
    
    # import pdb;pdb.set_trace()
    return ans




while True:
    sd = input()
    if not sd:
        break

    sd_list = list(map(int, sd.split(" ")))
    sd_list[1] = -sd_list[1]
    val = bactrack(sd_list)
    print(sum(val)) if sum(val)>0 else print("Deficit")
