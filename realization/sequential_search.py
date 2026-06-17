# 현재 위치(인덱스)를 저장할 수 있는 아주 간단한 포인터 클래스 정의
class Pointer:
    def __init__(self, start_index):
        self.idx = start_index

def sequential_search_curr(A, key):
    n = len(A)
    
    curr = Pointer(0)
    
    while curr.idx < n:
        
        # 현재 가리키는 위치(curr.idx)의 값과 key를 비교
        if A[curr.idx] == key:
            return curr.idx  # 찾으면 현재 인덱스 위치 반환
            
        # 일치하지 않으면 curr.idx를 다음 칸으로 한 칸 이동
        curr.idx += 1
        
    return -1  # 못 찾았으면 -1 반환

# --- 테스트 코드 ---
data = [25, 14, 9, 32, 78, 45]

print("현재 데이터:", data)

target = 9
result = sequential_search_curr(data, target)
print(f"curr.idx 방식으로 찾은 {target}의 위치: 인덱스 {result}")  # 출력 = 인덱스 2