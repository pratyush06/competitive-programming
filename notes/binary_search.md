# Binary Search

## Recognition Cues

- Search space is sorted or monotonic.
- Problem asks for minimum feasible, maximum feasible, first true, or last false.
- A direct answer can be checked faster than it can be constructed.

## Core Ideas

- Define the monotonic predicate before coding.
- Decide whether the answer is an index, value, or boundary.
- Use `while left < right` for boundary search.

## Common Traps

- Infinite loop from `mid` calculation or wrong pointer update.
- Mixing "first true" and "last true" logic.
- Returning `mid` instead of the final boundary.

## Review Problems

- `Recurrsion_problem/leet_code_binary_search_algo.py`
- `Recurrsion_problem/leet_code_search_insert_problem.py`
- `Recurrsion_problem/leet_code_278_first_bad_version.py`
- `divide_and_conquer/uva-12192-grapevine.py`

