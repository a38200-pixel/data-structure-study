# Python 자료구조 학습 정리

Python으로 자료구조와 알고리즘의 기본 개념을 학습하며 정리한 저장소입니다.  
학습 내용은 개인 정리 PDF를 기반으로 하되, 강의용 자료구조 PDF를 참고하여 부족했던 개념인 **ADT, 복잡도 분석, 연결 리스트, 트리, 그래프, 고급 정렬, 최소 비용 신장 트리** 등을 보강했습니다.

## 학습 목표

- 자료구조와 알고리즘의 관계 이해
- 선형 자료구조와 비선형 자료구조의 차이 정리
- 리스트, 스택, 큐, 덱, 집합, 맵의 ADT 관점 이해
- 정렬, 탐색, 해싱 알고리즘의 동작 원리와 시간 복잡도 정리
- 트리, 힙, 이진 탐색 트리, 그래프의 핵심 개념 정리
- Python 코드로 주요 자료구조를 직접 구현하며 동작 방식 확인

## 저장소 구조

```text
data-structure-study/
├── README.md
├── 01_data_structure_algorithm.md
├── 02_complexity_analysis.md
├── 03_list_set_adt.md
├── 04_stack_queue_deque.md
├── 05_linked_list.md
├── 06_sorting.md
├── 07_search_hashing_map.md
├── 08_tree_heap_bst.md
├── 09_graph_mst_shortest_path.md
├── 10_learning_log.md
├── examples/
│   ├── 01_list_adt.py
│   ├── 02_stack_maze.py
│   ├── 03_queue_priority_queue.py
│   ├── 04_linked_list.py
│   ├── 05_sorting_searching.py
│   ├── 06_hash_table.py
│   ├── 07_binary_tree.py
│   └── 08_graph_algorithms.py
└── docs/
    └── study_source_summary.md
```

## 학습 내용 요약

| 구분 | 핵심 내용 |
|---|---|
| 자료구조와 알고리즘 | 프로그램 = 자료구조 + 알고리즘, ADT, 선형/비선형 자료구조 |
| 복잡도 분석 | 시간 복잡도, 공간 복잡도, Big-O, Big-Ω, Big-Θ |
| 리스트와 집합 | 배열 기반 리스트, 연결 구조, 리스트 ADT, 집합 연산 |
| 스택/큐/덱 | LIFO, FIFO, 원형 큐, 우선순위 큐, 미로 탐색 |
| 연결 리스트 | 노드, 단순 연결 리스트, 원형 연결 리스트, 이중 연결 리스트 |
| 정렬 | 선택 정렬, 삽입 정렬, 버블 정렬, 병합/퀵/힙/기수 정렬 |
| 탐색과 해싱 | 순차 탐색, 이진 탐색, 보간 탐색, 해시 테이블, 충돌 처리 |
| 트리 | 이진 트리, 순회, 힙, 이진 탐색 트리, AVL 트리 |
| 그래프 | 인접 행렬/리스트, DFS, BFS, 위상 정렬, MST, 최단 경로 |

## 실행 방법

예제 코드는 `examples/` 폴더에 있습니다.

```bash
python examples/01_list_adt.py
python examples/05_sorting_searching.py
python examples/08_graph_algorithms.py
```

## 학습하며 느낀 점

자료구조는 단순히 문법을 외우는 내용이 아니라, **데이터를 어떤 방식으로 저장하고 접근할 것인지 결정하는 기준**이라는 점이 중요했습니다.  
같은 문제라도 배열, 연결 리스트, 스택, 큐, 트리, 그래프 중 어떤 구조를 선택하느냐에 따라 코드의 효율성과 구현 난이도가 달라진다는 점을 정리했습니다.

## 다음 학습 계획

- 리스트 ADT를 함수형 구현과 클래스 구현으로 각각 작성
- 스택 기반 DFS 미로 탐색과 큐 기반 BFS 미로 탐색 비교
- 원형 연결 리스트, 이중 연결 리스트 직접 구현
- 해시 테이블 충돌 처리 방식 비교
- 그래프 DFS/BFS, Kruskal, Prim, Dijkstra 알고리즘 코드 구현
