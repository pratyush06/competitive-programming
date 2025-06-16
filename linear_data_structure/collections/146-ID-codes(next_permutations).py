# UVA 146 - ID Codes
# Find the next lexicographically greater permutation of a string
# Input: String of lowercase letters, ends with "#"
# Output: Next permutation or "No Successor" if none exists

### this is example of next permutation algorithm 
# Use the next permutation algorithm when:

# You need the next lexicographically greater arrangement of a sequence (e.g., strings, numbers).
# Permutations are involved, but generating all permutations (O(n!)) is too slow.
# The problem asks for a sequence or arrangement just after the given one in sorted order.
# The sequence has duplicates (like "abaacb"), and you need to handle them correctly.

# Examples:
# UVA 146 - ID Codes: Find the next permutation of a string.
# LeetCode 31 - Next Permutation: Implement the algorithm for an array of integers.

def next_permutation(s: str) -> str:
    """Returns the next lexicographically greater permutation of string s."""
    # Convert string to list for manipulation
    arr = list(s)
    n = len(arr)
    
    # Step 1: Find first i from right where arr[i] < arr[i+1]
    # Find the first decreasing element from the end

    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i < 0:
        return "No Successor"  # Last permutation
    
    # Step 2: Find smallest j > i where arr[j] > arr[i]
    # Find the element just larger than nums[i] = 2 on the right

    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    
    # Step 3: Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]
    
    # Step 4: Reverse substring from i+1 to end
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return "".join(arr)

# Optional: Using collections.Counter for validation
from collections import Counter

def validate_input(s: str) -> bool:
    """Validates that the string contains only lowercase letters."""
    return all(c.islower() for c in s)

def main():
    while True:
        # Read input
        s = input().strip()
        
        # Check for termination
        if s == "#":
            break
            
        # Validate input (optional, using Counter for character check)
        # if not validate_input(s):
        #     print("Invalid input: Only lowercase letters allowed")
        #     continue
        
        # Get next permutation
        result = next_permutation(s)
        print(result)

if __name__ == "__main__":
    main()

# Example Usage:
# Input:
# abcd
# dcba
# #
# Output:
# abdc
# No Successor