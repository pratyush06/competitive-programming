# for binary indexing problem using pointer's like low and high is much more efficient than doing list slicing as list slicing will lead to creating new list everytime so could be slower than using pointer

input_string="aaaaaaaaaaaaaabbbbbbbbbdddddddddddccccccccccccc"
my_dict={}

for idx, k in enumerate(input_string):
    if k not in my_dict:
        my_dict[k]=[]
    my_dict[k].append(idx)

# def binary_search(current_state, my_list, low, high):
#     if low > high:
#         import pdb;pdb.set_trace()
#         # 'low' will be the index of the first element > current_state
#         return my_list[low]
    
#     mid = (low + high) // 2
    
#     # Even if we find a match, we keep looking to the right 
#     # to find the end of the sequence of identical values
#     if my_list[mid] <= current_state:
#         return binary_search(current_state, my_list, mid + 1, high)
#     else:
#         return binary_search(current_state, my_list, low, mid - 1)

def binary_search(current_state, my_list):
    if not my_list:
        return None
    mid = len(my_list) //2
    # if current state is greater or equal to than mid over ans definatley lies in other half
    if current_state>=my_list[mid]:
        return binary_search(current_state, my_list[mid+1:])
    # if current state is smaller than mid then our answer could mid or value which is smaller than mid but still greater than current state
    else:
        left_result = binary_search(current_state, my_list[:mid])
        if left_result is None:
            return my_list[mid]
        return left_result
        



# print(my_dict)


# print(binary_search(14, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

query1='aaaaaaaaaaaaaaaaaaa'
query2='aaaaaaaaaaabbbbbbbbbbbc'
query3='abccc'
current_state=-1
start_pointer= None
# end_pointer = None
for idx, i in enumerate(query3):
    if current_state==-1:
        current_state=my_dict[i][0]
        start_pointer=my_dict[i][0]
        continue
    # import pdb;pdb.set_trace()
    current_state=binary_search(current_state, my_dict[i])
    if current_state is None:
        print("Not Matched")
        break

if current_state is not None:
    print("Matched")
    print(f"start pointer {start_pointer}, end pointer {current_state}")