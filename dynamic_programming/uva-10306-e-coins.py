def backtrack(x, y, S_sq, coins, memo):
    current_e2 = x*x + y*y
    
    # Base Case: Hit the target exactly
    if current_e2 == S_sq:
        return 0 
    
    # Base Case: Exceeded the target
    if current_e2 > S_sq:
        return float('inf') 
        
    # Correct Memo lookup
    if memo[x][y] != -1:
        return memo[x][y]
    
    res = float('inf')
    for cx, cy in coins:
        # Skip (0,0) coins to avoid infinite recursion
        # if cx == 0 and cy == 0: continue
            
        sub_prob = backtrack(x + cx, y + cy, S_sq, coins, memo)
        
        if sub_prob != float('inf'):
            # Use min() with a high starting value
            res = min(res, 1 + sub_prob)
    
    memo[x][y] = res
    return res

# Correct Setup
coins = [(3,0), (0,4), (5,5)]
S = 5
S_sq = S * S
# Memo size must be at least S+1
memo = [[-1 for _ in range(S + 1)] for _ in range(S + 1)]

result = backtrack(0, 0, S_sq, coins, memo)
print(result if result != float('inf') else "not possible")