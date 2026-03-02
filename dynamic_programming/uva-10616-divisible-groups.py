def backtrack(elements, curr_idx, rem, no_of_element, memo, divisor, selected_ele):
    if curr_idx is None:
        curr_idx = 0
    
    # Base Case 1: We have picked the required number of elements (selected_ele)
    # We check if the current remainder is 0 (divisible) 🎯
    if no_of_element == selected_ele:
        return 1 if rem == 0 else 0
    
    # Base Case 2: We ran out of elements before picking enough ❌
    if curr_idx == len(elements):
        return 0
    
    # Memo Lookup: Using the remainder 'rem' as the index
    if memo[curr_idx][no_of_element][rem] is not None:
        return memo[curr_idx][no_of_element][rem]

    # Choice 1: Skip the current element
    val1 = backtrack(elements, curr_idx + 1, rem, no_of_element, memo, divisor, selected_ele)
    
    # Choice 2: Pick the current element
    # Instead of adding to a sum, we update the remainder using modulo 🔢
    # Python's % handles negative numbers correctly for this problem
    new_rem = (rem + elements[curr_idx]) % divisor
    val2 = backtrack(elements, curr_idx + 1, new_rem, no_of_element + 1, memo, divisor, selected_ele)
    
    memo[curr_idx][no_of_element][rem] = val1 + val2
    return val1 + val2

# Configuration
N = 10
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D_divisor = 5  # The number to divide by
M_selected = 2 # Number of elements to pick

# Memo size: [N][M+1][D_divisor]
memo = [[[None for _ in range(D_divisor)] for _ in range(M_selected + 1)] for _ in range(N)]

print(f"Total ways: {backtrack(elements, 0, 0, 0, memo, D_divisor, M_selected)}")
# print(memo)