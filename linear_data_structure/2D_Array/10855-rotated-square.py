def rotate_by_90(matrix, n):
    # Create a new n×n matrix for the 90-degree rotation
    ans = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n - 1 - i] = matrix[i][j]
    return ans

def all_submatrices(N, n, big_matrix):
    # Extract all possible n×n submatrices from N×N big_matrix
    submatrices = []
    for i in range(N - n + 1):
        for j in range(N - n + 1):
            sub = [row[j:j + n] for row in big_matrix[i:i + n]]
            submatrices.append(sub)
    return submatrices

def find_duplicates(submatrices, small_matrix):
    # Count how many submatrices match small_matrix
    return sum(1 for m in submatrices if m == small_matrix)

def main():
    while True:
        # Read N and n
        N, n = map(int, input().split())
        if N == 0 and n == 0:
            break
            
        # Read big and small matrices
        big_matrix = [list(input().strip()) for _ in range(N)]
        small_matrix = [list(input().strip()) for _ in range(n)]
        
        # Get all submatrices of big_matrix (do this once)
        submatrices = all_submatrices(N, n, big_matrix)
        
        # Initialize answer list for counts at 0°, 90°, 180°, 270°
        ans = []
        
        # Check small matrix at 0°
        count = find_duplicates(submatrices, small_matrix)
        ans.append(count)
        
        # Rotate small matrix 90°, 180°, 270° and check each
        for _ in range(3):
            small_matrix = rotate_by_90(small_matrix, n)
            count = find_duplicates(submatrices, small_matrix)
            ans.append(count)
        
        # Print counts space-separated
        print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()