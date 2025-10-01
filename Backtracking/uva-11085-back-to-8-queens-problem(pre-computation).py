
# ### ## [TECHNIQUE] The Pre-computation Method

# #### The Core Idea
# Pre-computation is an optimization technique where you solve the slow, repetitive part of a problem **once** at the beginning, store the results, and then use those stored results to answer each specific test case very quickly. It's a classic time-memory tradeoff.

# #### Why Our First Backtracking Solution Failed
# Our initial approach called the expensive backtracking function for **every single test case**. This was too slow and resulted in a **Time Limit Exceeded (TLE)** error because it repeatedly performed the same massive search for all 92 solutions again and again.

# #### How This Optimized Solution Works
# This solution is much faster because it splits the work into two distinct phases:

# 1.  **Phase 1 (Pre-computation):** At the very start of the program, we run the backtracking algorithm **exactly once** to find all 92 possible valid solutions for the 8-Queens problem. We store these solutions in a list.

# 2.  **Phase 2 (Processing Test Cases):** For each test case we read, we don't do any more backtracking. Instead, we perform a **fast** loop through our pre-computed list of 92 solutions, comparing each one to the input to find the minimum number of moves.

# This works because the set of all possible final answers is always the same. The only thing that changes per test case is the starting position we measure from. By calculating the hard part upfront, we make answering each test case trivial.

import sys

all_solutions = []
# We'll use 0-7 for rows internally to match list indices
board = [-1] * 8

def is_safe(row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for prev_col in range(col):
        prev_row = board[prev_col]
        # Check for same row or diagonal attack
        if prev_row == row or abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def generate_solutions(col=0):
    """A recursive function to find all 8-Queens solutions."""
    # Base Case: All 8 queens are placed successfully
    if col == 8:
        # Found a solution. Convert rows from 0-7 to 1-8 for the problem's format.
        all_solutions.append([r + 1 for r in board])
        return

    # Recursive Step: Try placing a queen in each row for the current column
    for row in range(8):
        if is_safe(row, col):
            board[col] = row
            generate_solutions(col + 1)

# --- This is the key: run the expensive part only one time at the start ---
generate_solutions()

# --- STEP 2: Process all test cases using the pre-computed list ---
case_num = 1
for line in sys.stdin:
    # Skip any empty or blank lines between test cases
    if not line.strip():
        continue
        
    initial_pos = list(map(int, line.split()))
    min_moves = 8 # The max possible moves is 8

    # This loop is VERY FAST!
    # It just compares the input to the 92 stored solutions.
    for solution in all_solutions:
        current_moves = 0
        for i in range(8):
            if initial_pos[i] != solution[i]:
                current_moves += 1
        min_moves = min(min_moves, current_moves)
        
    print(f"Case {case_num}: {min_moves}")
    case_num += 1