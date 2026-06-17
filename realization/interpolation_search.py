class Pointer:
    def __init__(self, low, high):
        self.low = low      # 시작 인덱스
        self.high = high    # 끝 인덱스
        self.pos = 0        # 값을 예측해서 찍을 인덱스 (이진 탐색의 mid 역할)

def interpolation_search_curr(A, key):
    curr = Pointer(0, len(A) - 1)
    
    # 보간 탐색은 찾으려는 key가 현재 탐색 범위(A[low] ~ A[high]) 안에 있을 때만 유효
    while curr.low <= curr.high and A[curr.low] <= key <= A[curr.high]:
        
        # 데이터가 비어있거나, 탐색 범위 양 끝의 값이 같을 때 분모가 0이 되는 것을 방지
        if A[curr.high] == A[curr.low]:
            if A[curr.low] == key:
                return curr.low
            break
            
        # key의 값에 따라 어디쯤 있을지 비례식으로 위치(pos)를 예측함
        # 결과가 소수점으로 나오므로 정수 인덱스로 바꾸기 위해 int() 사용
        curr.pos = curr.low + int((key - A[curr.low]) * (curr.high - curr.low) / (A[curr.high] - A[curr.low]))
        
        # 예측한 위치(A[curr.pos])에 찾던 key가 있으면 반환
        if A[curr.pos] == key:
            return curr.pos
            
        # 예측한 값보다 실제 key가 더 작다면? 왼쪽 범위를 보기 위해 high를 당김
        elif A[curr.pos] > key:
            curr.high = curr.pos - 1
            
        # 예측한 값보다 실제 key가 더 크다면? 오른쪽 범위를 보기 위해 low를 미룸
        else:
            curr.low = curr.pos + 1
            
    return -1  # 범위내에 없으면 -1 반환

# --- 테스트 코드 ---
sorted_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("정렬된 데이터:", sorted_data)
target = 90
result = interpolation_search_curr(sorted_data, target)
print(f"{target}의 위치: 인덱스 {result}")  # 출력: 인덱스 8