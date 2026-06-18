# Backtracking

## Recognition Cues

- Need all combinations, permutations, subsets, placements, or valid configurations.
- Choices form a decision tree.
- Constraints allow pruning.

## Core Ideas

- Track the current partial answer.
- Choose, recurse, then undo the choice.
- Use `start` index for combinations and `used` set/list for permutations.

## Common Traps

- Forgetting to undo state.
- Reusing elements when the problem forbids it.
- Appending the same mutable list instead of a copy.
- Not sorting when duplicate pruning depends on order.

## Review Problems

- `Backtracking/39_combination_sum_backtracking.py`
- `Backtracking/46_permutation.py`
- `Backtracking/n_queen_problem_backtracking.py`
- `Backtracking/Sudoku_Solver.py`
- `Backtracking/uva-524-prime-ring-problem.py`
