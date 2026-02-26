def coin_change(coins, total, memo):
    # Base Cases
    if total == 0: return 0
    if total < 0: return float('inf') # Use +inf for "Minimum" problems
    
    # Memo Lookup
    if memo[total] != -1:
        return memo[total]
    
    res = float('inf')
    
    # Try every coin at every step (this makes it "Infinite")
    for c in coins:
        sub_problem = coin_change(coins, total - c, memo)
        if sub_problem != float('inf'):
            res = min(res, 1 + sub_problem) # The "+1" counts the coin
            
    memo[total] = res
    return res

def get_coins_used(coins, amount, memo):
    path = []
    curr = amount
    while curr > 0:
        for c in coins:
            if curr - c >= 0 and memo[curr] == 1 + memo[curr - c]:
                path.append(c)
                curr -= c
                break
    return path

coins = [1, 2, 5]
total = 11
memo = [-1 for _ in range(total + 1)]
print(coin_change(coins, total, memo)) # Output: 3