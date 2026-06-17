# 06. 정렬 알고리즘

## 1. 정렬이란?

정렬(Sorting)은 데이터를 특정 기준에 따라 순서대로 재배열하는 작업입니다.  
정렬은 탐색, 집합 연산, 데이터 분석 등 많은 작업의 전처리 과정으로 활용됩니다.

## 2. 정렬의 분류

| 기준 | 분류 |
|---|---|
| 정렬 장소 | 내부 정렬, 외부 정렬 |
| 알고리즘 효율성 | 단순 정렬, 고급 정렬 |
| 안정성 | 안정 정렬, 불안정 정렬 |
| 추가 공간 사용 | 제자리 정렬, 비제자리 정렬 |
| 비교 여부 | 비교 기반 정렬, 비비교 정렬 |

## 3. 선택 정렬

선택 정렬은 정렬되지 않은 구간에서 가장 작은 값을 선택해 앞쪽으로 보내는 방식입니다.

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        least = i

        for j in range(i + 1, n):
            if arr[j] < arr[least]:
                least = j

        arr[i], arr[least] = arr[least], arr[i]

    return arr
```

| 항목 | 내용 |
|---|---|
| 시간 복잡도 | O(n²) |
| 제자리 정렬 | 가능 |
| 안정 정렬 | 일반 구현에서는 불안정 |

## 4. 삽입 정렬

삽입 정렬은 이미 정렬된 구간에 새로운 값을 알맞은 위치에 삽입하는 방식입니다.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
```

| 항목 | 내용 |
|---|---|
| 최선 | O(n) |
| 평균/최악 | O(n²) |
| 특징 | 거의 정렬된 데이터에 효율적 |
| 안정 정렬 | 가능 |

## 5. 버블 정렬

버블 정렬은 인접한 두 값을 비교하여 순서가 맞지 않으면 교환하는 방식입니다.

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        changed = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changed = True

        if not changed:
            break

    return arr
```

| 항목 | 내용 |
|---|---|
| 최선 | O(n) |
| 평균/최악 | O(n²) |
| 특징 | 이해하기 쉽지만 비효율적 |
| 안정 정렬 | 가능 |

## 6. 병합 정렬

병합 정렬은 리스트를 절반씩 나누고 정렬된 결과를 병합하는 분할 정복 방식입니다.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

| 항목 | 내용 |
|---|---|
| 시간 복잡도 | O(n log n) |
| 안정 정렬 | 가능 |
| 단점 | 추가 메모리 필요 |

## 7. 퀵 정렬

퀵 정렬은 피벗을 기준으로 작은 값과 큰 값을 나누고 재귀적으로 정렬하는 방식입니다.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
```

| 항목 | 내용 |
|---|---|
| 평균 | O(n log n) |
| 최악 | O(n²) |
| 특징 | 평균적으로 빠름 |
| 단점 | 피벗 선택에 따라 성능 차이 큼 |

## 8. 힙 정렬

힙 정렬은 힙 자료구조의 루트에 최댓값 또는 최솟값이 위치하는 성질을 이용합니다.

```python
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    result = []

    while arr:
        result.append(heapq.heappop(arr))

    return result
```

| 항목 | 내용 |
|---|---|
| 시간 복잡도 | O(n log n) |
| 특징 | 우선순위 큐와 관련 |
| 안정 정렬 | 일반적으로 불안정 |

## 9. 정렬 알고리즘 비교

| 정렬 | 평균 | 최악 | 안정성 | 특징 |
|---|---:|---:|---|---|
| 선택 정렬 | O(n²) | O(n²) | 불안정 | 교환 횟수가 적음 |
| 삽입 정렬 | O(n²) | O(n²) | 안정 | 거의 정렬된 데이터에 강함 |
| 버블 정렬 | O(n²) | O(n²) | 안정 | 구현이 쉬움 |
| 병합 정렬 | O(n log n) | O(n log n) | 안정 | 추가 메모리 필요 |
| 퀵 정렬 | O(n log n) | O(n²) | 불안정 | 평균적으로 빠름 |
| 힙 정렬 | O(n log n) | O(n log n) | 불안정 | 힙 사용 |

## 10. 핵심 정리

- 선택, 삽입, 버블 정렬은 단순하지만 대체로 O(n²)이다.
- 병합 정렬은 안정적이고 O(n log n)이지만 추가 공간이 필요하다.
- 퀵 정렬은 평균적으로 빠르지만 최악의 경우 O(n²)이다.
- 힙 정렬은 우선순위 큐의 원리를 활용한다.
