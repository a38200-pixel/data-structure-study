# 03. 리스트와 집합 ADT

## 1. 리스트란?

리스트(List)는 항목들이 차례대로 나열되어 있는 선형 자료구조입니다.  
각 항목은 위치 또는 인덱스를 가지며, 원하는 위치에 삽입하거나 삭제할 수 있습니다.

Python의 기본 `list`는 배열 기반 구조에 가깝습니다.

```python
numbers = [10, 20, 30]
print(numbers[0])   # 10
numbers.append(40)
```

## 2. 배열 구조와 연결 구조

리스트를 구현하는 방식은 크게 배열 구조와 연결 구조로 나눌 수 있습니다.

| 구분 | 배열 구조 | 연결 구조 |
|---|---|---|
| 저장 방식 | 연속된 공간에 저장 | 노드들이 링크로 연결 |
| 인덱스 접근 | 빠름 | 순차 이동 필요 |
| 삽입/삭제 | 중간 삽입/삭제 시 이동 비용 발생 | 링크 조정으로 처리 가능 |
| 용량 | 고정 또는 재할당 필요 | 동적으로 확장 가능 |
| 대표 예 | Python list | Linked List |

## 3. 리스트 ADT

리스트 ADT는 다음 연산을 제공할 수 있습니다.

| 연산 | 설명 |
|---|---|
| `insert(pos, item)` | 특정 위치에 항목 삽입 |
| `delete(pos)` | 특정 위치의 항목 삭제 |
| `is_empty()` | 리스트가 비어 있는지 확인 |
| `is_full()` | 리스트가 가득 찼는지 확인 |
| `get_entry(pos)` | 특정 위치의 항목 반환 |
| `size()` | 항목 개수 반환 |
| `clear()` | 리스트 초기화 |
| `find(item)` | 항목의 위치 탐색 |
| `replace(pos, item)` | 특정 위치의 항목 교체 |
| `sort()` | 정렬 |
| `merge(list)` | 다른 리스트와 병합 |
| `display()` | 리스트 출력 |
| `append(item)` | 맨 뒤에 항목 추가 |

## 4. 배열 기반 리스트 ADT 예시

```python
class ArrayList:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def insert(self, pos, item):
        if self.is_full():
            raise IndexError("리스트가 가득 찼습니다.")
        if pos < 0 or pos > self.count:
            raise IndexError("삽입 위치가 올바르지 않습니다.")

        for i in range(self.count, pos, -1):
            self.items[i] = self.items[i - 1]

        self.items[pos] = item
        self.count += 1

    def delete(self, pos):
        if self.is_empty():
            raise IndexError("리스트가 비어 있습니다.")
        if pos < 0 or pos >= self.count:
            raise IndexError("삭제 위치가 올바르지 않습니다.")

        removed = self.items[pos]

        for i in range(pos, self.count - 1):
            self.items[i] = self.items[i + 1]

        self.items[self.count - 1] = None
        self.count -= 1
        return removed

    def display(self):
        print(self.items[:self.count])
```

## 5. 집합이란?

집합(Set)은 중복을 허용하지 않는 자료구조입니다.  
수학의 집합처럼 합집합, 교집합, 차집합 같은 연산을 수행할 수 있습니다.

Python에는 기본적으로 `set` 자료형이 있습니다.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합
```

## 6. 정렬된 리스트 기반 집합

집합을 정렬된 리스트로 구현하면 합집합, 교집합 같은 연산에서 두 포인터를 이용할 수 있습니다.

```python
def union_sorted(a, b):
    result = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

## 7. 핵심 정리

- 리스트는 순서가 있는 선형 자료구조이다.
- 배열 구조는 인덱스 접근이 빠르지만 삽입/삭제 비용이 클 수 있다.
- 연결 구조는 삽입/삭제에 유리하지만 임의 접근은 느리다.
- 집합은 중복을 허용하지 않는 자료구조이다.
- 정렬된 집합은 합집합/교집합 연산을 효율적으로 구현할 수 있다.
