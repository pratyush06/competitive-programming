# Competitive Programming Interview Recall

This repository is a personal practice archive for competitive programming, data structures, algorithms, and related learning projects.

Use this page as the fast-recall entry point before interviews: start from the pattern, review the cue, scan the template, then solve one or two representative problems without looking.

## Quick Review Flow

1. Pick the pattern from the interview index below.
2. Read the recognition cues and common traps in `notes/`.
3. Open the matching template in `templates/`.
4. Re-solve one problem from the must-review list.
5. Update `revision_tracker.md` with confidence and next review date.

## Interview Index

| Pattern | Notes | Template | Practice folders |
| --- | --- | --- | --- |
| Arrays and hashing | [notes/arrays_hashing.md](notes/arrays_hashing.md) | - | [Hashing](Hashing), [linear_data_structure/1D_Array](linear_data_structure/1D_Array) |
| Two pointers | [notes/two_pointers.md](notes/two_pointers.md) | [templates/two_pointers.py](templates/two_pointers.py) | [two_pointers](two_pointers) |
| Binary search | [notes/binary_search.md](notes/binary_search.md) | [templates/binary_search.py](templates/binary_search.py) | [divide_and_conquer](divide_and_conquer), [Recurrsion_problem](Recurrsion_problem) |
| Backtracking | [notes/backtracking.md](notes/backtracking.md) | [templates/backtracking.py](templates/backtracking.py) | [Backtracking](Backtracking) |
| Dynamic programming | [notes/dynamic_programming.md](notes/dynamic_programming.md) | [templates/dynamic_programming.py](templates/dynamic_programming.py) | [dynamic_programming](dynamic_programming) |
| Graphs | [notes/graphs.md](notes/graphs.md) | [templates/graphs.py](templates/graphs.py) | [graph_problem](graph_problem) |
| Greedy | [notes/greedy.md](notes/greedy.md) | - | [greedy_problems](greedy_problems) |
| Heaps and priority queues | [notes/heaps.md](notes/heaps.md) | [templates/heap.py](templates/heap.py) | [non_linear_data_structure/priority_queue](non_linear_data_structure/priority_queue) |

## Must-Review Problems

Keep this list short. These are the problems worth revisiting when interview time is close.

| Problem | Pattern | File |
| --- | --- | --- |
| Course Schedule | Graph cycle detection / topological sort | [graph_problem/207_course_schedule_topological_sort.py](graph_problem/207_course_schedule_topological_sort.py) |
| Number of Islands | DFS / BFS flood fill | [graph_problem/200_number_of_islands_dfs_flood_fill.py](graph_problem/200_number_of_islands_dfs_flood_fill.py) |
| Network Delay Time | Dijkstra / shortest path | [graph_problem/743_network_delay_time_dijkstra.py](graph_problem/743_network_delay_time_dijkstra.py) |
| Wormholes | Bellman-Ford / negative cycle | [graph_problem/uva_558_wormholes_bellman_ford.py](graph_problem/uva_558_wormholes_bellman_ford.py) |
| Longest Increasing Subsequence | DP / binary search | [dynamic_programming/300_longest_increasing_subsequence_dp.py](dynamic_programming/300_longest_increasing_subsequence_dp.py) |
| Partition Equal Subset Sum | 0/1 knapsack | [dynamic_programming/416_partition_equal_subset_sum_knapsack.py](dynamic_programming/416_partition_equal_subset_sum_knapsack.py) |
| Maximum Subarray | Kadane's algorithm | [dynamic_programming/53_maximum_subarray_kadane.py](dynamic_programming/53_maximum_subarray_kadane.py) |
| Combination Sum | Backtracking | [Backtracking/39_combination_sum_backtracking.py](Backtracking/39_combination_sum_backtracking.py) |
| N Queens | Backtracking constraints | [Backtracking/n_queen_problem_backtracking.py](Backtracking/n_queen_problem_backtracking.py) |
| Container With Most Water | Two pointers | [two_pointers/11_container_with_most_water_two_pointers.py](two_pointers/11_container_with_most_water_two_pointers.py) |
| Merge Sorted Array | Two pointers from end | [two_pointers/88_merge_sorted_array_two_pointers.py](two_pointers/88_merge_sorted_array_two_pointers.py) |

## Solution Header Template

Add this header to important solutions as you revisit them.

```python
"""
Pattern:
Recognition cue:
Key idea:
Time:
Space:
Common traps:
"""
```

## Non-Interview Learning Areas

These folders are useful learning material, but they live outside the fastest DSA interview review path:

- `learning_projects/flask_tutorials/`
- `learning_projects/DRF_projects/`
- `learning_projects/dbt_projects/`
- `SOLID_PRINCIPLES/`
