# Two Pointers

## Recognition Cues

- Input is sorted, can be sorted, or asks for a pair/subsequence.
- Need compare values from both ends.
- Need remove duplicates or merge arrays in-place.

## Core Template

- Start `left = 0`, `right = len(nums) - 1`.
- Move the pointer that cannot be part of a better answer.
- Preserve the invariant after every move.

## Common Traps

- Moving both pointers when only one side is proven impossible.
- Losing in-place data while merging from the front.
- Forgetting duplicate skipping in k-sum style problems.

## Review Problems

- `two_pointers/11_container_with_most_water.py`
- `two_pointers/3sum_two_pointer.py`
- `two_pointers/88_merge_sorted_Array.py`
- `two_pointers/350_intersection_two_array.py`

