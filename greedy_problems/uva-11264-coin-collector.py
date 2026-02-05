no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    no_of_coins = int(input())
    coin_values = list(map(int, input().split()))
    max_no_of_coins = []
    for idx, c in enumerate(coin_values):
        if idx==0 or len(coin_values)==idx+1:
            max_no_of_coins.append(c)
        elif (sum(max_no_of_coins)+c)<coin_values[idx+1]:
            max_no_of_coins.append(c)
    
    print(f" Answers {max_no_of_coins}, total no of coins {len(max_no_of_coins)}")
