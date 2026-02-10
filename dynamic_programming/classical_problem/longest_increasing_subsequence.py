def lis_classic(arr):
    if not arr:
        return 0
    
    n = len(arr)
    # dp[i] stores the length of the LIS ending at index i
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# Example:
data = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Classic LIS Length: {lis_classic(data)}") # Output: 4 (2, 3, 7, 18)


import bisect

def lis_patient_sorting(arr):
    if not arr:
        return 0
    
    # tails[i] is the smallest tail of all increasing subsequences of length i+1
    tails = []
    
    for x in arr:
        # Use binary search to find the leftmost spot where x can be placed
        idx = bisect.bisect_left(tails, x)
        
        if idx < len(tails):
            # If x is smaller than an existing tail, replace it
            # This makes the sequence more "extendable" in the future
            tails[idx] = x
        else:
            # If x is larger than all current tails, it extends the LIS
            tails.append(x)
            
    return len(tails)

# Example:
data = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Patient Sorting LIS Length: {lis_patient_sorting(data)}") # Output: 4