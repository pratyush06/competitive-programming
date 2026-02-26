def train_sort(weights):
    n = len(weights)
    lis = [1] * n
    lds = [1] * n
    
    # Process from right to left
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if weights[i] < weights[j]:
                # Car j is heavier -> can go in front
                # This contributes to increasing sequence from i
                lis[i] = max(lis[i], 1 + lis[j])
            elif weights[i] > weights[j]:
                # Car j is lighter -> can go in back
                # This contributes to decreasing sequence from i
                lds[i] = max(lds[i], 1 + lds[j])
    
    # Find the best starting car
    max_length = 0
    for i in range(n):
        # we are doing -1 bcz largest element will present at end of lis and at begenning of lds
        max_length = max(max_length, lis[i] + lds[i] - 1)
    
    return max_length

# Test with your example
data = [3, 1, 2, 3]
result = train_sort(data)
print(f"Maximum train length: {result}")

# Let's trace through to see why