def kadane(arr):
    max_so_far = -float('inf')
    current_max = 0
    for x in arr:
        current_max = max(x, current_max + x)
        max_so_far = max(max_so_far, current_max)
    return max_so_far


def max_sum_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    global_max = -float('inf')

    for r1 in range(rows):
        # Temporary array to store column sums
        temp = [0] * cols
        for r2 in range(r1, rows):
            for c in range(cols):
                temp[c] += matrix[r2][c]
            
            # Use Kadane on the compressed 1D array
            current_kadane = kadane(temp)
            global_max = max(global_max, current_kadane)
            
    return global_max

