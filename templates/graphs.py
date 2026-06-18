from collections import defaultdict, deque
import heapq


def build_adj_list(n, edges, directed=False):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph


def bfs(start, graph):
    seen = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                queue.append(nei)

    return order


def topological_sort(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([node for node in range(n) if indegree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return order if len(order) == n else []


def dijkstra(n, graph, source):
    dist = [float("inf")] * n
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue

        for nei, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                heapq.heappush(heap, (new_cost, nei))

    return dist


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1

        return True

