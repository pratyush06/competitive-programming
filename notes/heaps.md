# Heaps and Priority Queues

## Recognition Cues

- Need repeated min or max extraction.
- Need top `k`, merge sorted streams, schedule tasks, or process events by priority.
- A sorted list would be too expensive to maintain.

## Core Ideas

- Python `heapq` is a min-heap.
- Use negative values for max-heap behavior.
- Store tuples like `(priority, tie_breaker, item)` when priorities can tie.

## Common Traps

- Forgetting lazy deletion when priorities change.
- Comparing objects directly in heap tuples.
- Using heap when a deque is enough for BFS.

## Review Problems

- `non_linear_data_structure/priority_queue/11995-I_Can_Guess_the_Data_Structure.py`
- `non_linear_data_structure/priority_queue`
- `Recurrsion_problem/cpu_task_schedular.py`

