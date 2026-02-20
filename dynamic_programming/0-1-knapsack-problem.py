def place(remCap, item_weight):
    return remCap >= item_weight

def backtrack(value, weight, cap, memo, curr_idx=None):
    if curr_idx is None:
        curr_idx =0
    # Base Case: No more capacity or no more items
    if cap == 0 or curr_idx == len(weight):
        return 0
    
    # Memo Lookup: Check for the REMAINING CAPACITY (cap), not item weight
    if memo[curr_idx][cap] != -1:
        return memo[curr_idx][cap]
    
    # Path 1: Skip the current item (This is ALWAYS an option)
    res = backtrack(value, weight, cap, memo, curr_idx + 1)
    
    # Path 2: Take the current item (Only if it fits)
    if place(cap, weight[curr_idx]):
        take_value = value[curr_idx] + backtrack(value, weight, cap - weight[curr_idx], memo, curr_idx + 1)
        res = max(res, take_value)
    
    # Save the result for this SPECIFIC capacity
    memo[curr_idx][cap] = res
    return res

def get_selected_items(value, weight, cap, memo):
    selected_indices = []
    current_cap = cap
    
    for i in range(len(weight)):
        # If we are at the last item, we check if it was included
        if i == len(weight) - 1:
            if current_cap >= weight[i] and memo[i][current_cap] > 0:
                selected_indices.append(i)
            break

        # Check: Is the best value at this state the SAME as the best value 
        # we would get by skipping this item?
        skip_value = memo[i + 1][current_cap]
        
        if memo[i][current_cap] != skip_value:
            # If values are different, it means skipping wasn't the best choice.
            # Therefore, we must have TAKEN this item.
            selected_indices.append(i)
            current_cap -= weight[i]
            
    return selected_indices

# After running your backtrack function:
indices = get_selected_items(v, w, cap, memo)
print(f"Chosen Indices: {indices}")

v = [60, 100, 120]
w = [10, 20, 30]
cap = 50
# Initialize memo with -1
memo = [[-1 for _ in range(cap + 1)] for _ in range(len(w))]

print(f"Max Value: {backtrack(v, w, cap, memo)}")