# Arrays and Hashing

## Recognition Cues

- Need fast membership, frequency, or last-seen lookup.
- Problem asks for pairs, duplicates, anagrams, counts, or grouping.
- Brute force repeatedly scans the same values.

## Core Ideas

- Use a set for existence.
- Use a dict for counts, indexes, or grouping keys.
- Convert a repeated lookup from O(n) to O(1) average time.

## Common Traps

- Forgetting negative numbers or zero.
- Updating the hashmap before checking when order matters.
- Using a mutable object as a dict key.
- Missing case sensitivity or character set assumptions.

## Review Problems

- `Sorting_problem/two_sum.py`
- `two_pointers/217_contains_dplicate.py`
- `Hashing/longest_substring_without_repeting_character.py`
- `Hashing/int_to_roman.py`

