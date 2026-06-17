# 04. 스택, 큐, 덱, 우선순위 큐

## 1. 스택(Stack)

스택은 **후입선출(LIFO, Last-In First-Out)** 구조입니다.  
마지막에 들어온 데이터가 가장 먼저 나갑니다.

대표적인 예시는 다음과 같습니다.

- 문서 편집기의 되돌리기
- 웹 브라우저 뒤로 가기
- 함수 호출 스택
- 괄호 검사
- DFS 기반 미로 탐색
- 후위 표기식 계산

## 2. 스택 ADT

| 연산 | 설명 |
|---|---|
| `push(item)` | 항목 삽입 |
| `pop()` | top 항목 삭제 후 반환 |
| `peek()` | top 항목 확인 |
| `is_empty()` | 비어 있는지 확인 |

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
```

## 3. 큐(Queue)

큐는 **선입선출(FIFO, First-In First-Out)** 구조입니다.  
먼저 들어온 데이터가 먼저 나갑니다.

대표적인 예시는 다음과 같습니다.

- 인쇄 작업 큐
- 은행 대기표
- 콜센터 대기열
- 버퍼
- BFS 그래프 탐색
- 공항 활주로 이용 순서

## 4. 큐 ADT

| 연산 | 설명 |
|---|---|
| `enqueue(item)` | rear에 항목 삽입 |
| `dequeue()` | front에서 항목 삭제 후 반환 |
| `peek()` | front 항목 확인 |
| `is_empty()` | 비어 있는지 확인 |

```python
from collections import deque

queue = deque()
queue.append("A")
queue.append("B")
print(queue.popleft())  # A
```

## 5. 원형 큐

단순 배열 큐는 앞쪽 공간이 비어도 다시 사용하기 어렵습니다.  
원형 큐는 배열을 원형처럼 사용하여 공간 낭비를 줄입니다.

핵심 아이디어는 인덱스를 증가시킬 때 나머지 연산을 사용하는 것입니다.

```python
rear = (rear + 1) % capacity
front = (front + 1) % capacity
```

## 6. 덱(Deque)

덱은 Double Ended Queue의 줄임말입니다.  
양쪽 끝에서 삽입과 삭제가 모두 가능합니다.

```python
from collections import deque

dq = deque()
dq.append(1)       # 오른쪽 삽입
dq.appendleft(0)   # 왼쪽 삽입
dq.pop()           # 오른쪽 삭제
dq.popleft()       # 왼쪽 삭제
```

## 7. 우선순위 큐

우선순위 큐는 먼저 들어온 순서가 아니라 **우선순위가 높은 데이터가 먼저 나오는 큐**입니다.

활용 예시는 다음과 같습니다.

- 운영체제 작업 스케줄링
- 네트워크 트래픽 제어
- 시뮬레이션
- 다익스트라 최단 경로 알고리즘
- 허프만 코딩

Python에서는 `heapq` 모듈을 이용해 최소 힙 기반 우선순위 큐를 만들 수 있습니다.

```python
import heapq

pq = []
heapq.heappush(pq, (2, "보통 작업"))
heapq.heappush(pq, (1, "중요 작업"))

print(heapq.heappop(pq))  # (1, '중요 작업')
```

## 8. 핵심 정리

- 스택은 LIFO 구조이다.
- 큐는 FIFO 구조이다.
- 덱은 양쪽 끝에서 삽입/삭제가 가능하다.
- 우선순위 큐는 입력 순서보다 우선순위가 중요하다.
- DFS는 스택, BFS는 큐를 활용하는 대표적인 예시이다.
