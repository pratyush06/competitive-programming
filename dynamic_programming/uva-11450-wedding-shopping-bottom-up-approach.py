# reference https://gemini.google.com/share/e84526dd6c98

def main():
    try:
        line = input().split()
        if not line: return
        no_of_test_cases = int(line[0])
    except EOFError:
        return

    for _ in range(no_of_test_cases):
        # Read M and C
        # M = budget, C = number of garment categories
        M, C = map(int, input().split())
        
        # reachable[garment_id][money_spent]
        # Rows: 0 to C-1 (garments)
        # Cols: 0 to M (money spent)
        reachable = [[False] * (M + 1) for _ in range(C)]
        
        # --- Handle the first garment separately to bootstrap the DP ---
        first_garment_line = list(map(int, input().split()))
        # first_garment_line[0] is K (number of models), the rest are prices
        for price in first_garment_line[1:]:
            if price <= M:
                reachable[0][price] = True
        
        # --- Process the rest of the garments (from 1 to C-1) ---
        for g in range(1, C):
            current_garment_line = list(map(int, input().split()))
            prices = current_garment_line[1:] # Skip the count K
            
            for spent in range(M + 1):
                # If it was possible to spend 'spent' amount on previous garments
                if reachable[g-1][spent]:
                    for p in prices:
                        if spent + p <= M:
                            reachable[g][spent + p] = True
        
        # --- Final result is the highest 'True' index in the last garment row ---
        ans = -1
        for spent in range(M, -1, -1):
            if reachable[C-1][spent]:
                ans = spent
                break
        
        if ans == -1:
            print("no solution")
        else:
            print(ans)

if __name__ == "__main__":
    main()

### reference function to understand how to get optimal choices along with optimal answer
# choices = []
#         current_spent = max_spent
        
#         for g in range(C - 1, 0, -1): # Work backwards from last garment to second
#             for p in all_prices[g]:
#                 prev_spent = current_spent - p
#                 if prev_spent >= 0 and reachable[g-1][prev_spent]:
#                     choices.append(p)
#                     current_spent = prev_spent
#                     break # Found a valid path for this garment
        
#         # The very first garment is the remainder
#         choices.append(current_spent)
        
#         # Reverse because we collected them from last to first
#         choices.reverse()
        
#         print(f"Max Spent: {max_spent}")
#         print(f"Prices: {' '.join(map(str, choices))}")