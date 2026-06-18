# Dynamic Programming

## Recognition Cues

- Choices overlap and the same subproblem repeats.
- Problem asks for count, min, max, feasibility, or best score.
- Brute force recursion repeats work.

## Core Ideas

- Define state: what information uniquely describes a subproblem?
- Define transition: how does one choice move to a smaller state?
- Define base cases before the loop or recursion.
- Choose top-down when state is clearer; bottom-up when ordering is easy.

## Common Traps

- State misses one variable, causing accidental reuse.
- Wrong iteration direction in 0/1 knapsack.
- Confusing subsequence with substring.
- Forgetting impossible-state initialization.

## Review Problems

- `dynamic_programming/70_climbing_stairs.py`
- `dynamic_programming/53_maximum_subarray.py`
- `dynamic_programming/300_longest_incresing_subsequence.py`
- `dynamic_programming/416_partion_equal_subset_sum.py`
- `dynamic_programming/uva-11450-wedding-shopping-bottom-up-approach.py`
