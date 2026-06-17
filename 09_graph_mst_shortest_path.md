# 09. 그래프, MST, 최단 경로

## 1. 그래프란?

그래프(Graph)는 객체들 사이의 관계를 표현하는 자료구조입니다.

```text
G = (V, E)
```

| 기호 | 의미 |
|---|---|
| V | 정점(Vertex)의 집합 |
| E | 간선(Edge)의 집합 |

그래프는 지하철 노선도, 네트워크 연결, 도로망, SNS 친구 관계 등 복잡한 연결 관계를 표현할 때 사용됩니다.

## 2. 그래프 종류

| 종류 | 설명 |
|---|---|
| 무방향 그래프 | 간선에 방향이 없음 |
| 방향 그래프 | 간선에 방향이 있음 |
| 가중치 그래프 | 간선에 비용이나 가중치가 있음 |
| 부분 그래프 | 기존 그래프의 일부 정점과 간선으로 구성 |
| 연결 그래프 | 모든 정점 사이에 경로가 존재 |

## 3. 그래프 표현 방법

## 인접 행렬

정점 간 연결 여부를 2차원 배열로 표현합니다.

| 장점 | 단점 |
|---|---|
| 연결 여부 확인이 빠름 | 정점 수가 많으면 메모리 낭비 |

```python
graph = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]
```

## 인접 리스트

각 정점에 연결된 정점 목록을 저장합니다.

| 장점 | 단점 |
|---|---|
| 간선이 적은 그래프에 효율적 | 연결 여부 확인은 상대적으로 느림 |

```python
graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"]
}
```

## 4. DFS

DFS(Depth First Search)는 깊이 우선 탐색입니다.  
한 방향으로 최대한 깊게 들어간 뒤, 더 이상 갈 곳이 없으면 되돌아옵니다.

스택 또는 재귀를 이용해 구현할 수 있습니다.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for nxt in graph[start]:
        if nxt not in visited:
            dfs(graph, nxt, visited)
```

## 5. BFS

BFS(Breadth First Search)는 너비 우선 탐색입니다.  
시작 정점에서 가까운 정점부터 차례대로 방문합니다.

큐를 이용해 구현합니다.

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
```

## 6. 연결 성분

연결 성분은 서로 연결되어 있는 정점들의 최대 부분 그래프입니다.  
그래프가 여러 덩어리로 나뉘어 있는지 확인할 때 사용합니다.

## 7. 신장 트리

신장 트리는 그래프의 모든 정점을 포함하면서 사이클이 없는 트리입니다.  
정점이 `n`개라면 신장 트리는 항상 `n-1`개의 간선을 가집니다.

## 8. 최소 비용 신장 트리

MST(Minimum Spanning Tree)는 신장 트리 중 간선 가중치의 합이 최소인 트리입니다.

활용 예시는 다음과 같습니다.

- 통신망 설계
- 도로망 설계
- 전기 배선
- 배관 설계

대표 알고리즘은 Kruskal과 Prim입니다.

## 9. Kruskal 알고리즘

Kruskal 알고리즘은 간선을 가중치 오름차순으로 정렬한 뒤, 사이클이 생기지 않는 간선을 선택합니다.  
사이클 검사는 Union-Find 자료구조를 사용합니다.

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False
```

## 10. 위상 정렬

위상 정렬은 방향 그래프에서 선행 순서를 만족하도록 정점을 나열하는 방법입니다.  
사이클이 없는 방향 그래프(DAG)에서만 가능합니다.

활용 예시는 다음과 같습니다.

- 선수 과목 순서
- 작업 스케줄링
- 빌드 순서 결정

## 11. 최단 경로

가중치 그래프에서 한 정점에서 다른 정점까지 비용이 가장 작은 경로를 찾는 문제입니다.

| 알고리즘 | 특징 |
|---|---|
| Dijkstra | 하나의 시작 정점에서 다른 모든 정점까지 최단 경로 |
| Floyd-Warshall | 모든 정점 쌍 사이의 최단 경로 |

## 12. 핵심 정리

- 그래프는 복잡한 연결 관계를 표현한다.
- 인접 행렬은 연결 여부 확인이 빠르지만 메모리를 많이 쓴다.
- 인접 리스트는 간선이 적은 그래프에 효율적이다.
- DFS는 깊이 우선, BFS는 너비 우선 탐색이다.
- MST는 모든 정점을 최소 비용으로 연결하는 트리이다.
- Kruskal은 간선 중심, Prim은 정점 확장 중심의 MST 알고리즘이다.
- Dijkstra와 Floyd-Warshall은 최단 경로 문제에 사용된다.
