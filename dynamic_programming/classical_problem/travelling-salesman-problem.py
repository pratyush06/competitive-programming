from math import inf

def place(mask, i):
    # Returns True if the i-th bit is 0 (not visited)
    return not (mask & (1 << i))

def backtrack(distances, N, mask, current_city, memo):
    # Base Case: All cities visited
    if mask == (1 << N) - 1:
        return distances[current_city][0]
    
    # Memoization check
    if memo[mask][current_city] != -1:
        return memo[mask][current_city]
    
    best_distance = inf

    for i in range(N):
        if place(mask, i):
            # Move to city i and mark it as visited in the mask
            new_dist = distances[current_city][i] + backtrack(distances, N, mask | (1 << i), i, memo)
            best_distance = min(best_distance, new_dist)

    memo[mask][current_city] = best_distance
    return best_distance

def get_path(distances, N, memo):
    path = [0] # Start at City 0
    mask = 1   # City 0 is visited
    u = 0      # Current city
    
    while len(path) < N:
        for v in range(N):
            # 1. Check if City v is unvisited
            if not (mask & (1 << v)):
                # 2. Check if moving to v is optimal
                # Cost to move to v + Optimal cost from v == Optimal cost from u
                if distances[u][v] + memo[mask | (1 << v)][v] == memo[mask][u]:
                    path.append(v)
                    mask |= (1 << v)
                    u = v
                    break
    
    path.append(0) # Return to start
    return path

# --- Setup and Execution ---
n = 4
distances = [
    [0, 1, 1.41, 1],
    [1, 0, 1, 1.41],
    [1.41, 1, 0, 1],
    [1, 1.41, 1, 0]
]
memo = [[-1 for _ in range(n)] for _ in range(1 << n)]

# Start at city 0, with city 0 marked as visited (mask = 1)
print(f"Shortest Path: {backtrack(distances, n, 1, 0, memo)}")