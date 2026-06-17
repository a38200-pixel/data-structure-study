# 07. 탐색, 해싱, 맵

## 1. 탐색이란?

탐색(Search)은 데이터 집합에서 원하는 키를 가진 항목을 찾는 작업입니다.

예시는 다음과 같습니다.

- 상품 코드로 상품 찾기
- 사전에서 단어 찾기
- 학생 번호로 학생 정보 찾기
- 웹 검색에서 키워드 찾기

## 2. 순차 탐색

순차 탐색은 처음부터 끝까지 하나씩 비교하는 방법입니다.

```python
def sequential_search(arr, key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1
```

| 항목 | 내용 |
|---|---|
| 장점 | 구현이 쉽고 정렬이 필요 없음 |
| 단점 | 데이터가 많으면 느림 |
| 시간 복잡도 | O(n) |

## 3. 이진 탐색

이진 탐색은 정렬된 데이터에서 가운데 값을 기준으로 탐색 범위를 절반씩 줄입니다.

```python
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

| 항목 | 내용 |
|---|---|
| 조건 | 데이터가 정렬되어 있어야 함 |
| 장점 | 빠름 |
| 시간 복잡도 | O(log n) |

## 4. 보간 탐색

보간 탐색은 이진 탐색처럼 범위를 줄이지만, 항상 중앙을 보는 것이 아니라 값의 분포를 이용해 위치를 예측합니다.

적합한 경우:

- 데이터가 정렬되어 있음
- 값이 비교적 균일하게 분포함

```python
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= key <= arr[high]:
        if arr[high] == arr[low]:
            break

        pos = low + int((key - arr[low]) * (high - low) / (arr[high] - arr[low]))

        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1
```

## 5. 맵과 딕셔너리

맵(Map)은 키와 값을 한 쌍으로 저장하는 자료구조입니다.

```python
student = {
    "name": "Kim",
    "score": 90
}

print(student["name"])
```

Python의 `dict`는 해시 테이블을 기반으로 구현되어 있어 평균적으로 빠른 검색, 삽입, 삭제가 가능합니다.

## 6. 해싱

해싱(Hashing)은 키 값에 해시 함수를 적용하여 저장 위치를 계산하는 방법입니다.

```text
key -> hash function -> hash address
```

해싱을 사용하면 평균적으로 `O(1)`에 가까운 탐색 성능을 기대할 수 있습니다.

## 7. 해시 충돌

서로 다른 키가 같은 해시 주소를 갖는 경우를 충돌(Collision)이라고 합니다.  
충돌은 해시 테이블에서 반드시 고려해야 하는 문제입니다.

## 8. 충돌 처리 방법

| 방법 | 설명 |
|---|---|
| 선형 조사법 | 다음 빈 칸을 순서대로 찾음 |
| 이차 조사법 | 제곱 간격으로 다음 위치 탐색 |
| 이중 해싱 | 두 번째 해시 함수를 사용 |
| 체이닝 | 하나의 버킷에 여러 값을 연결 리스트로 저장 |

## 9. 체이닝 예시

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_func(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_func(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return None
```

## 10. 핵심 정리

- 순차 탐색은 간단하지만 O(n)이다.
- 이진 탐색은 정렬된 데이터에서 O(log n)이다.
- 보간 탐색은 균일한 데이터 분포에서 효과적이다.
- 맵은 키-값 구조이다.
- 해싱은 평균적으로 빠른 탐색을 가능하게 한다.
- 해시 충돌은 선형 조사, 이차 조사, 이중 해싱, 체이닝으로 처리할 수 있다.
