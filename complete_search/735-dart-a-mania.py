from itertools import combinations_with_replacement, permutations

# Prepare all valid dart throws
throws = []
for i in range(1, 21):
    throws.append(('S', i, i))        # Single
    throws.append(('D', i, 2 * i))    # Double
    throws.append(('T', i, 3 * i))    # Triple
throws.append(('S', 25, 50))          # Bullseye
throws.append(('S',     0, 0))

# Read input scores
while True:
    score = int(input())
    if score <= 0:
        print("END OF OUTPUT")
        break

    # Store unique combinations (set of 3 throws, regardless of order)
    combination_set = set()
    permutation_set = set()

    for t1 in throws:
        for t2 in throws:
            for t3 in throws:
                if t1[2] + t2[2] + t3[2] == score:
                    # Sorted tuple of throw descriptions → combination
                    sorted_comb = tuple(sorted([t1[2], t2[2], t3[2]]))
                    combination_set.add(sorted_comb)

                    # Actual sequence of throws → permutation
                    permutation_set.add((t1[2], t2[2], t3[2]))

    # print(combination_set   )
    if not combination_set:
        print(f"THE SCORE OF {score} CANNOT BE MADE WITH THREE DARTS.")
    else:
        print(f"NUMBER OF COMBINATIONS THAT SCORES {score} IS {len(combination_set)}.")
        print(f"NUMBER OF PERMUTATIONS THAT SCORES {score} IS {len(permutation_set)}.")
    print("**********************************************************************")
