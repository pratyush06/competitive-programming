# Graphs

## Recognition Cues

- Entities and relationships appear: courses, roads, dependencies, islands, networks.
- Need reachability, shortest path, connected components, or ordering.
- Constraints mention `n` nodes and edge lists.

## Pattern Map

| Need | Pattern |
| --- | --- |
| Explore all reachable nodes | DFS / BFS |
| Fewest edges in unweighted graph | BFS |
| Shortest weighted path with non-negative weights | Dijkstra |
| Detect negative cycle | Bellman-Ford |
| Dependencies / prerequisites | Topological sort |
| Group connected nodes dynamically | Union find |
| Strongly connected components | Tarjan / Kosaraju |

## Common Traps

- Treating directed edges as undirected.
- Marking visited too late in BFS.
- Forgetting disconnected components.
- Using Dijkstra with negative weights.
- Recursion depth issues on large DFS.

## Review Problems

- `graph_problem/200_number_of_islands.py`
- `graph_problem/207_course_schedule.py`
- `graph_problem/743_network_delay_time.py`
- `graph_problem/uva-558-wormholes.py`
- `graph_problem/union-find.py`
- `graph_problem/classical_problem/topological_sort.py`

