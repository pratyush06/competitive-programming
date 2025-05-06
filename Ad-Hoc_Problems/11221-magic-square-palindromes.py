import string
import math

def is_magic_square(s):
    # Clean string
    cleaned = ''.join(c for c in s if c not in string.whitespace and c not in string.punctuation)
    n = len(cleaned)

    # Check if length is a perfect square
    # we need to take sqrt bcz let's number is 10 and 2 divides 10 but 2*2 matrix only fit's 4 character not 10 so we need perfect saure
    root = int(math.sqrt(n))
    if root * root != n:
        return None

    # Check if it's a palindrome
    if cleaned != cleaned[::-1]:
        return None

    # Build grid
    grid = [cleaned[i*root:(i+1)*root] for i in range(root)]
    import pdb;pdb.set_trace()
    # Read column-wise
    col_read = ''.join(grid[j][i] for i in range(root) for j in range(root))

    # Read reversed row-wise
    rev_row = ''.join(grid[i][j] for i in reversed(range(root)) for j in reversed(range(root)))

    # Read reversed column-wise
    rev_col = ''.join(grid[j][i] for i in reversed(range(root)) for j in reversed(range(root)))

    # Check all reads match the original
    if col_read == cleaned and rev_row == cleaned and rev_col == cleaned:
        return root
    return None

# Main logic
no_of_test = int(input())
for t in range(1, no_of_test + 1):
    sentence = input()
    result = is_magic_square(sentence)
    print(f"Case #{t}:")
    if result:
        print(result)
    else:
        print("No magic :(")
