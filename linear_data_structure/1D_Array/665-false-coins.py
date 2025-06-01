# intersection update method in set data structure insert common element from both
# diffrence update remove common element for target set 
# set add method add single element
# while update add a iterable e.g list
no_of_test_cases = int(input())

for i in range(no_of_test_cases):
    # Initialize candidate sets for lighter and heavier coins
    lighter = set()
    heavier = set()
    
    # Read blank line
    input()
    
    # Read number of coins (N) and weighings (K)
    no_of_coins, weighings = map(int, input().split())
    
    # Initially, all coins could be lighter or heavier
    for coin in range(1, no_of_coins + 1):
        lighter.add(coin)
        heavier.add(coin)
    
    # Process each weighing
    for _ in range(int(weighings)):
        weight = list(map(int, input().split()))
        p = weight[0]  # Number of coins in each pan
        left_pan = weight[1:p+1]  # Coins in left pan
        right_pan = weight[p+1:2*p+1]  # Coins in right pan
        result = input().strip()  # Weighing result (<, >, =)
        
        if result == '<':
            # Left < Right: Left coins could be lighter, Right coins could be heavier
            lighter.intersection_update(left_pan)
            heavier.intersection_update(right_pan)
            lighter.difference_update(set(range(1, no_of_coins + 1)) - set(left_pan + right_pan))
            heavier.difference_update(set(range(1, no_of_coins + 1)) - set(left_pan + right_pan))
        elif result == '>':
            # Left > Right: Left coins could be heavier, Right coins could be lighter
            heavier.intersection_update(left_pan)
            lighter.intersection_update(right_pan)
            lighter.difference_update(set(range(1, no_of_coins + 1)) - set(left_pan + right_pan))
            heavier.difference_update(set(range(1, no_of_coins + 1)) - set(left_pan + right_pan))
        else:  # result == '='
            # Balanced: All coins in both pans are genuine
            lighter.difference_update(left_pan + right_pan)
            heavier.difference_update(left_pan + right_pan)
    
    # Find the counterfeit coin
    candidates = lighter.union(heavier)
    if len(candidates) == 1:
        print(candidates.pop())  # Output the single counterfeit coin
    else:
        print(0)  # No unique solution
    
    # Add blank line between test cases, but not after the last one
    if i < no_of_test_cases - 1:
        print()