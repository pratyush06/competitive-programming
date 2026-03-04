"""
WHY 2D ARRAY (OR COIN-FIRST LOOP)?
1. Combinations vs Permutations: This problem asks for combinations (order doesn't matter).
   Your original code counts permutations because it allows any coin at any time, 
   treating [1, 5] and [5, 1] as two different ways.
   
2. The Second Dimension (Coin Index): To avoid duplicates, we must force an order 
   (e.g., use all 1s, then all 5s). We need the 'coin index' in our state to 
   ensure we never 'look back' at a coin we've already finished using.

3. Difference from 'Min Coins': In Min Coins, multiple paths to the same total 
   don't matter because min(2, 2) is still 2. In Counting, every path is 
   added (1 + 1 = 2), so we must restrict the paths to a single, unique order.
"""

def place(total, c):
    return True if total - c>=0 else False


def backtrack(coins, memo, total, curr_idx):
    if total<0 or curr_idx==len(coins):
        return 0
    if total==0:
        return 1
    if memo[curr_idx][total]!= -1:
        memo[curr_idx][total]


    res1 = backtrack(coins, memo, total-coins[curr_idx], curr_idx)
    res2 = backtrack(coins, memo, total, curr_idx+1)
    memo[curr_idx][total] = res1 + res2
    return res1 + res2





coins = [1, 5, 10, 25, 50]
total = 17
memo = [[-1 for _ in range(total+1) ] for _ in range(len(coins)) ]
print(backtrack(coins, memo, total, 0))
print(memo)