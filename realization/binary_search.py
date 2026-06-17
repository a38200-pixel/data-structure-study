class Pointer:
    def __init__(self, low, high):
        self.low = low      # 시작 인덱스
        self.high = high    # 끝 인덱스
        self.mid = 0        # 중앙 인덱스

def binary_search_curr(A, key):
    # 이진 탐색을 시작할 때, curr 객체에 처음(0)과 끝(len-1) 위치를 담음
    curr = Pointer(0, len(A) - 1)
    
    # 시작점(low)이 끝점(high)보다 작거나 같을 때까지 반복
    while curr.low <= curr.high:
        
        # 중앙 위치(mid) 계산 (소수점은 버림)
        curr.mid = (curr.low + curr.high) // 2
        
        # 중앙에 있는 값(A[curr.mid])이 내가 찾는 key면 반환
        if A[curr.mid] == key:
            return curr.mid
            
        # 중앙 값보다 key가 더 작다면? 왼쪽 절반을 보기 위해 high를 당김
        elif A[curr.mid] > key:
            curr.high = curr.mid - 1
            
        # 중앙 값보다 key가 더 크다면? 오른쪽 절반을 보기 위해 low를 미룸.
        else:
            curr.low = curr.mid + 1
            
    return -1  # 범위내에 없으면 -1 반환

# --- 테스트 코드 ---
sorted_data = [10, 20, 30, 40, 50, 60, 70]

print("정렬된 데이터:", sorted_data)

target = 60
result = binary_search_curr(sorted_data, target)
print(f"{target}의 위치: 인덱스 {result}")  # 출력: 인덱스 5