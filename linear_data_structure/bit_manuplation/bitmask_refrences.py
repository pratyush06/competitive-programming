# Bit Manipulation Revision Guide
# For learning bitsets, bitmasks, and solving UVa 10264 - The Most Potent Corner
# Updated with comments on where to use each bitmask operation
# Concepts covered: Bitwise operations, bitsets, bitmasks, hypercube neighbors, UVa 10264 solution
# Prepared for revising competitive programming bit manipulation in Python

# -----------------------------------
# 1. Bitwise Operations Example (Unchanged)
# -----------------------------------
def bitwise_operations_example():
    print("=== Bitwise Operations Example ===")
    a, b = 5, 3  # a = 0101, b = 0011 (4-bit representation)
    
    # AND: 1 if both bits are 1
    print(f"AND: {a} & {b} = {a & b}")  # 0101 & 0011 = 0001 = 1
    
    # OR: 1 if at least one bit is 1
    print(f"OR: {a} | {b} = {a | b}")   # 0101 | 0011 = 0111 = 7
    
    # XOR: 1 if bits differ
    print(f"XOR: {a} ^ {b} = {a ^ b}")  # 0101 ^ 0011 = 0110 = 6
    
    # NOT: Flips bits (careful: Python uses signed integers)
    print(f"NOT: ~{a} = {~a}")         # ~0101 = 1010 (but signed, so -6)
    
    # Left Shift: Multiply by 2^shift
    print(f"Left Shift: {a} << 1 = {a << 1}")  # 0101 << 1 = 1010 = 10
    
    # Right Shift: Divide by 2^shift
    print(f"Right Shift: {a} >> 1 = {a >> 1}") # 0101 >> 1 = 0010 = 2

# -----------------------------------
# 2. Bitset Simulation in Python
# -----------------------------------
def integer_bitset_example():
    print("\n=== Integer Bitset Example ===")
    bitset = 0  # 0000... (empty bitset)
    
    # Set bit at position 2
    # WHERE TO USE: Add an element to a set, enable a flag, or mark a state as active (e.g., in bitmask DP to mark a visited node).
    bitset |= (1 << 2)  # 0100 (4 in decimal)
    print(f"Set bit 2: {bin(bitset)[2:].zfill(4)}")
    
    # Check if bit 2 is set
    # WHERE TO USE: Check if an element is in a set, a flag is enabled, or a state is active (e.g., in subset enumeration or DP to verify node inclusion).
    if bitset & (1 << 2):
        print("Bit 2 is set")
    
    # Toggle bit 2
    # WHERE TO USE: Flip a state (on to off or off to on), such as switching a flag or navigating to a neighbor in a hypercube (e.g., UVa 10264 neighbor detection).
    bitset ^= (1 << 2)  # 0000
    print(f"Toggle bit 2: {bin(bitset)[2:].zfill(4)}")
    
    # Set multiple bits (0 and 3)
    # WHERE TO USE: Initialize a set with multiple elements or combine states (e.g., in knapsack or subset problems to include multiple items).
    bitset |= (1 << 0) | (1 << 3)  # 1001 (9 in decimal)
    print(f"Set bits 0,3: {bin(bitset)[2:].zfill(4)}")
    
    # Count set bits (Brian Kernighan's algorithm)
    # WHERE TO USE: Count elements in a set or active states (e.g., in problems like LeetCode 191: Number of 1 Bits).
    def count_set_bits(n):
        count = 0
        while n:
            n &= (n - 1)  # Clear least significant set bit
            count += 1
        return count
    print(f"Number of set bits: {count_set_bits(bitset)}")  # 2

# Optional: Using bitarray (install with `pip install bitarray`)
try:
    from bitarray import bitarray
    def bitarray_example():
        print("\n=== Bitarray Example ===")
        bits = bitarray(10)  # 10-bit array
        bits.setall(0)  # 0000000000
        print(f"Initial: {bits}")
        
        # Set bits
        bits[2] = bits[5] = 1
        print(f"Set bits 2,5: {bits}")
        
        # Check bit
        print(f"Bit 2 is: {bits[2]}")  # True
        
        # Count set bits
        print(f"Set bits count: {bits.count(1)}")  # 2
        
        # Bitwise operations
        other = bitarray('0011000000')
        print(f"AND with {other}: {bits & other}")
except ImportError:
    def bitarray_example():
        print("\n=== Bitarray Example ===\nInstall bitarray with `pip install bitarray` to run.")

# -----------------------------------
# 3. Bitmask Techniques
# -----------------------------------
def subset_enumeration_example(n=3):
    print("\n=== Subset Enumeration Example ===")
    # Iterate over all possible bitmasks
    # WHERE TO USE: Generate all subsets or combinations of n elements (e.g., in knapsack, subset sum, or combinatorial problems like LeetCode 78: Subsets).
    for mask in range(1 << n):  # 0 to 2^n - 1
        subset = []
        # Check each bit to build subset
        # WHERE TO USE: Identify which elements are included in a subset (e.g., in UVa 10264 to inspect corner coordinates or in subset enumeration).
        for i in range(n):
            if mask & (1 << i):
                subset.append(i)
        print(f"Mask: {bin(mask)[2:].zfill(n)}, Subset: {subset}")

def tsp_example():
    print("\n=== Bitmask DP Example (TSP) ===")
    n = 3
    graph = [
        [0, 10, 15],
        [10, 0, 35],
        [15, 35, 0]
    ]
    dp = [[float('inf')] * n for _ in range(1 << n)]
    # Initialize starting state
    # WHERE TO USE: Set initial state in bitmask DP (e.g., mark starting node as visited in TSP).
    dp[1][0] = 0  # Start at city 0
    
    # Iterate over all subsets of visited nodes
    # WHERE TO USE: Explore all possible states in DP (e.g., in TSP, knapsack, or other state-space problems).
    for mask in range(1 << n):
        for curr in range(n):
            # Check if current city is visited
            # WHERE TO USE: Verify if a node/state is active in the current mask (e.g., in TSP to skip unvisited cities).
            if not (mask & (1 << curr)):
                continue
            for next_city in range(n):
                # Check if next city is unvisited
                # WHERE TO USE: Check if a state can be transitioned to (e.g., in TSP to add an unvisited city).
                if not (mask & (1 << next_city)):
                    # Add next city to the mask
                    # WHERE TO USE: Transition to a new state by adding an element (e.g., in DP to include a new node/item).
                    new_mask = mask | (1 << next_city)
                    dp[new_mask][next_city] = min(
                        dp[new_mask][next_city],
                        dp[mask][curr] + graph[curr][next_city]
                    )
    
    all_visited = (1 << n) - 1
    min_cost = float('inf')
    for last in range(n):
        if last == 0:
            continue
        min_cost = min(min_cost, dp[all_visited][last] + graph[last][0])
    print(f"Minimum TSP cost: {min_cost}")

# -----------------------------------
# 4. UVa 10264 - The Most Potent Corner
# -----------------------------------
def uva_10264_solution():
    print("\n=== UVa 10264 Solution ===")
    while True:
        try:
            N = int(input("Enter N (dimension, or Ctrl+D for EOF): "))
        except EOFError:
            print("End of input")
            break
        
        # Compute number of corners
        # WHERE TO USE: Calculate total states (e.g., number of vertices in a hypercube or subsets in combinatorial problems).
        num_corners = 1 << N  # 2^N corners
        weights = [int(input(f"Enter weight for corner {i}: ")) for i in range(num_corners)]
        print(f"Weights: {weights}")
        
        # Compute potency for each corner
        potencies = [0] * num_corners
        for corner in range(num_corners):
            for bit in range(N):
                # Find neighbor by flipping one bit
                # WHERE TO USE: Navigate to adjacent states in a graph where edges represent single-bit differences (e.g., hypercube neighbors in UVa 10264).
                neighbor = corner ^ (1 << bit)  # XOR flips one bit
                potencies[corner] += weights[neighbor]
            print(f"Corner {corner} ({bin(corner)[2:].zfill(N)}): Potency = {potencies[corner]}")
        
        # Find max sum of potencies for neighboring corners
        max_sum = 0
        for corner in range(num_corners):
            for bit in range(N):
                # Check each neighbor
                # WHERE TO USE: Revisit neighbors to compute properties over graph edges (e.g., sum of potencies in UVa 10264).
                neighbor = corner ^ (1 << bit)
                curr_sum = potencies[corner] + potencies[neighbor]
                print(f"Pair ({corner}, {neighbor}): Sum = {curr_sum}")
                max_sum = max(max_sum, curr_sum)
        
        print(f"Maximum potency sum: {max_sum}")

# -----------------------------------
# 5. Understanding Neighbors with XOR
# -----------------------------------
def visualize_neighbors(N=3, corner=5):
    print(f"\n=== Visualize Neighbors (N={N}, Corner={corner}) ===")
    print(f"Corner {bin(corner)[2:].zfill(N)} neighbors:")
    for bit in range(N):
        # Create single-bit mask
        # WHERE TO USE: Generate a mask to target a specific bit for flipping or checking (e.g., in hypercube graphs or state transitions).
        mask = 1 << bit
        # Find neighbor by flipping one bit
        # WHERE TO USE: Compute adjacent vertices in a hypercube or toggle a state (e.g., UVa 10264 neighbor detection).
        neighbor = corner ^ mask
        print(f"Flip bit {bit} (mask {bin(mask)[2:].zfill(N)}): {bin(neighbor)[2:].zfill(N)} ({neighbor})")

# -----------------------------------
# 6. Useful Bit Manipulation Tricks
# -----------------------------------
def bit_tricks():
    print("\n=== Bit Manipulation Tricks ===")
    
    # Check if power of 2
    # WHERE TO USE: Validate if a number has exactly one bit set (e.g., in problems checking powers of 2 or single-bit states).
    def is_power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0
    print(f"Is 8 power of 2? {is_power_of_two(8)}")  # True
    
    # Get lowest set bit
    # WHERE TO USE: Extract the least significant set bit (e.g., in algorithms processing bits one by one, like bit counting).
    def lowest_set_bit(n):
        return n & -n
    print(f"Lowest set bit of 10 (1010): {lowest_set_bit(10)}")  # 2
    
    # Turn off rightmost set bit
    # WHERE TO USE: Remove the least significant set bit (e.g., in Brian Kernighan’s algorithm for counting set bits).
    def turn_off_rightmost(n):
        return n & (n - 1)
    print(f"Turn off rightmost bit of 10 (1010): {turn_off_rightmost(10)}")  # 8
    
    # Swap two numbers
    # WHERE TO USE: Swap values without a temporary variable (rare in competitive programming but useful for understanding XOR).
    def swap(a, b):
        a ^= b; b ^= a; a ^= b
        return a, b
    a, b = 5, 10
    a, b = swap(a, b)
    print(f"Swap 5, 10: {a}, {b}")  # 10, 5

# -----------------------------------
# 7. Practice Exercises
# -----------------------------------
# To revise, try these:
# 1. Modify uva_10264_solution to print the pair of corners giving max sum.
# 2. Write a function to count set bits using bin().count('1') and compare with Brian Kernighan's.
# 3. Implement subset enumeration for N=4 and print only subsets with exactly 2 elements.
# 4. Test visualize_neighbors with different N and corners.

if __name__ == "__main__":
    print("Running Bit Manipulation Revision Examples")
    bitwise_operations_example()
    integer_bitset_example()
    bitarray_example()
    subset_enumeration_example()
    tsp_example()
    visualize_neighbors()
    bit_tricks()
    print("\nRun uva_10264_solution() manually with input to test.")
    # Example input for UVa 10264:
    # 2
    # 1
    # 2
    # 3
    # 4
    # (Uncomment and run uva_10264_solution() to test with input)