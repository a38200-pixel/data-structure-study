# Python 자료구조 학습 정리

Python으로 자료구조와 알고리즘의 기본 개념을 학습하며 정리한 저장소입니다.  
개인 학습 정리 PDF를 기반으로 하되, 강의용 자료구조 PDF를 참고하여 부족했던 개념인 **ADT, 복잡도 분석, 연결 리스트, 트리, 그래프, 고급 정렬, 최소 비용 신장 트리** 등을 보강했습니다.

이 저장소는 단순 개념 정리뿐 아니라, 직접 작성하며 연습한 Python 구현 파일을 함께 보관하여 자료구조의 동작 방식을 코드로 확인하는 것을 목표로 합니다.

---

## 학습 목표

- 자료구조와 알고리즘의 관계 이해
- 선형 자료구조와 비선형 자료구조의 차이 정리
- 리스트, 스택, 큐, 덱, 집합, 맵의 ADT 관점 이해
- 정렬, 탐색, 해싱 알고리즘의 동작 원리와 시간 복잡도 정리
- 트리, 힙, 이진 탐색 트리, AVL 트리, 그래프의 핵심 개념 정리
- Python 코드로 주요 자료구조를 직접 구현하며 동작 방식 확인
- 예제 코드와 개인 실습 코드를 분리하여 학습 과정 관리

---

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
├── realization/
│   ├── ArrayList.py
│   ├── set.py
│   ├── stack.py
│   ├── que_linear.py
│   ├── que_circle.py
│   ├── priority_que.py
│   ├── deck_linear.py
│   ├── deck_circle.py
│   ├── single_linked_list.py
│   ├── Linked_list.py
│   ├── circular_linked_list.py
│   ├── doubly_linked_list.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── bubble_sort.py
│   ├── sequential_search.py
│   ├── binary_search.py
│   ├── interpolation_search.py
│   ├── hashing.py
│   ├── tree.py
│   ├── binary_search_tree.py
│   ├── avl_tree.py
│   ├── heap_huffman.py
│   ├── miro.py
│   ├── miro_strategic.py
│   └── miro_width.py
└── docs/
    └── study_source_summary.md
```

---

## 학습 내용 요약

| 구분 | 핵심 내용 |
|---|---|
| 자료구조와 알고리즘 | 프로그램 = 자료구조 + 알고리즘, ADT, 선형/비선형 자료구조 |
| 복잡도 분석 | 시간 복잡도, 공간 복잡도, Big-O, Big-Ω, Big-Θ |
| 리스트와 집합 | 배열 기반 리스트, 연결 구조, 리스트 ADT, 집합 연산 |
| 스택/큐/덱 | LIFO, FIFO, 원형 큐, 우선순위 큐, 덱 |
| 연결 리스트 | 노드, 단순 연결 리스트, 원형 연결 리스트, 이중 연결 리스트 |
| 정렬 | 선택 정렬, 삽입 정렬, 버블 정렬 |
| 탐색과 해싱 | 순차 탐색, 이진 탐색, 보간 탐색, 해시 테이블 |
| 트리 | 이진 트리, 이진 탐색 트리, AVL 트리, 힙, 허프만 트리 |
| 그래프/탐색 응용 | DFS, BFS, 미로 탐색 문제 |

---

## 문서 정리 파일

| 파일 | 내용 |
|---|---|
| `01_data_structure_algorithm.md` | 자료구조와 알고리즘의 기본 개념 |
| `02_complexity_analysis.md` | 시간 복잡도, 공간 복잡도, 점근적 표기 |
| `03_list_set_adt.md` | 리스트와 집합 ADT |
| `04_stack_queue_deque.md` | 스택, 큐, 덱 |
| `05_linked_list.md` | 연결 리스트 구조 |
| `06_sorting.md` | 선택/삽입/버블 정렬 중심 정리 |
| `07_search_hashing_map.md` | 탐색 알고리즘과 해싱 |
| `08_tree_heap_bst.md` | 트리, 힙, 이진 탐색 트리 |
| `09_graph_mst_shortest_path.md` | 그래프와 그래프 알고리즘 |
| `10_learning_log.md` | 학습 기록 및 느낀 점 |

---

## 예제 코드와 개인 구현 코드 구분

이 저장소는 `examples/`와 `realization/` 폴더를 구분하여 관리합니다.

| 폴더 | 역할 |
|---|---|
| `examples/` | 개념 설명을 위해 정리한 대표 예제 코드 |
| `realization/` | 학습 과정에서 직접 작성하고 연습한 구현 코드 |

`examples/`는 README와 각 `.md` 문서에서 설명한 개념을 빠르게 확인하기 위한 예제 중심 코드입니다.  
`realization/`은 수업과 개인 학습 과정에서 직접 구현한 코드들을 보관하는 폴더입니다.

---

## realization 폴더 실습 파일 분류

### 리스트와 집합

| 파일 | 내용 |
|---|---|
| `ArrayList.py` | 배열 기반 리스트 구현 |
| `set.py` | 집합 ADT 및 집합 연산 구현 |

### 스택, 큐, 덱

| 파일 | 내용 |
|---|---|
| `stack.py` | 스택 구현 |
| `que_linear.py` | 선형 큐 구현 |
| `que_circle.py` | 원형 큐 구현 |
| `priority_que.py` | 우선순위 큐 구현 |
| `deck_linear.py` | 선형 덱 구현 |
| `deck_circle.py` | 원형 덱 구현 |

### 연결 리스트

| 파일 | 내용 |
|---|---|
| `single_linked_list.py` | 단순 연결 리스트 구현 |
| `Linked_list.py` | 연결 리스트 구현 연습 |
| `circular_linked_list.py` | 원형 연결 리스트 구현 |
| `doubly_linked_list.py` | 이중 연결 리스트 구현 |

### 정렬

| 파일 | 내용 |
|---|---|
| `selection_sort.py` | 선택 정렬 구현 |
| `insertion_sort.py` | 삽입 정렬 구현 |
| `bubble_sort.py` | 버블 정렬 구현 |

### 탐색과 해싱

| 파일 | 내용 |
|---|---|
| `sequential_search.py` | 순차 탐색 구현 |
| `binary_search.py` | 이진 탐색 구현 |
| `interpolation_search.py` | 보간 탐색 구현 |
| `hashing.py` | 해싱 구조 구현 |

### 트리

| 파일 | 내용 |
|---|---|
| `tree.py` | 기본 트리 구조 구현 |
| `binary_search_tree.py` | 이진 탐색 트리 구현 |
| `avl_tree.py` | AVL 트리 구현 |
| `heap_huffman.py` | 힙과 허프만 트리 관련 구현 |

### 미로 탐색 응용

| 파일 | 내용 |
|---|---|
| `miro.py` | 미로 탐색 기본 구현 |
| `miro_strategic.py` | 전략 기반 미로 탐색 구현 |
| `miro_width.py` | 너비 우선 탐색 기반 미로 탐색 구현 |

---

## 실행 방법

예제 코드는 `examples/` 폴더에서 실행할 수 있습니다.

```bash
python examples/01_list_adt.py
python examples/05_sorting_searching.py
python examples/08_graph_algorithms.py
```

개인 구현 코드는 `realization/` 폴더에서 실행할 수 있습니다.

```bash
python realization/ArrayList.py
python realization/stack.py
python realization/que_circle.py
python realization/selection_sort.py
python realization/binary_search_tree.py
python realization/avl_tree.py
```

파일명에 따라 대소문자가 구분될 수 있으므로, GitHub에 올린 실제 파일명과 실행 명령어의 파일명이 일치하는지 확인해야 합니다.

---

## 학습하며 느낀 점

자료구조는 단순히 문법을 외우는 내용이 아니라, **데이터를 어떤 방식으로 저장하고 접근할 것인지 결정하는 기준**이라는 점이 중요했습니다.  

같은 문제라도 배열, 연결 리스트, 스택, 큐, 트리, 그래프 중 어떤 구조를 선택하느냐에 따라 코드의 효율성과 구현 난이도가 달라집니다.  
특히 리스트, 스택, 큐처럼 단순해 보이는 구조도 직접 구현해보니 내부 동작 방식과 시간 복잡도를 더 명확하게 이해할 수 있었습니다.

또한 `examples/` 폴더의 대표 예제와 `realization/` 폴더의 직접 구현 코드를 분리하면서, 개념 정리와 실습 기록을 함께 관리하는 방식이 GitHub 학습 기록에 더 적합하다고 느꼈습니다.

---

## 다음 학습 계획

- 리스트 ADT를 함수형 구현과 클래스 구현으로 각각 비교
- 스택 기반 DFS 미로 탐색과 큐 기반 BFS 미로 탐색 비교
- 원형 연결 리스트와 이중 연결 리스트 코드 개선
- 해시 테이블 충돌 처리 방식 비교
- 이진 탐색 트리와 AVL 트리 삽입/삭제 과정 정리
- 그래프 DFS/BFS, Kruskal, Prim, Dijkstra 알고리즘 추가 구현
