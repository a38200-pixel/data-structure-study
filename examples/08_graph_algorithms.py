from collections import deque


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for nxt in graph[start]:
        if nxt not in visited:
            order.extend(dfs(graph, nxt, visited))

    return order


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

    return order


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False

    parent[root_b] = root_a
    return True


def kruskal(vertices, edges):
    parent = {v: v for v in vertices}
    mst = []
    total = 0

    for weight, a, b in sorted(edges):
        if union(parent, a, b):
            mst.append((a, b, weight))
            total += weight

    return mst, total


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }

    print("DFS:", dfs(graph, "A"))
    print("BFS:", bfs(graph, "A"))

    vertices = ["A", "B", "C", "D"]
    edges = [
        (1, "A", "B"),
        (4, "A", "C"),
        (2, "B", "C"),
        (3, "B", "D"),
        (5, "C", "D"),
    ]

    mst, total = kruskal(vertices, edges)
    print("MST:", mst)
    print("총 비용:", total)
