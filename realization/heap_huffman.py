class MinHeap:
    def __init__(self):
        # 인덱스 계산을 쉽게 하기 위해 0번 방은 비워두고 1번부터 사용
        self.heap = [None]

    # 삽입 연산 : 새 데이터를 맨 뒤에 넣고 부모와 비교하며 위로 올림
    def insert(self, data):
        self.heap.append(data)
        curr = len(self.heap) - 1 # 새로 추가된 노드의 위치
        
        while curr > 1:
            parent = curr // 2
            # 최소 힙: 내가 부모보다 '작으면' 자리를 바꿈
            if self.heap[curr] < self.heap[parent]:
                self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
                curr = parent
            else: 
                break

    # 삭제 연산: 최솟값(루트 노드)을 뽑아내고, 맨 뒤 노드를 올려 밑으로 내림
    def delete(self):
        if len(self.heap) <= 1: return None
        
        min_val = self.heap[1]     # 탈출시킬 최솟값(루트 노드) 백업
        last_val = self.heap.pop() # 맨 마지막 말단 노드 추출
        
        if len(self.heap) > 1:
            self.heap[1] = last_val # 말단 노드를 임시로 루트 자리에 앉힘
            curr = 1                # 루트에서부터 탐색 출발
            
            while curr * 2 < len(self.heap): # 자식 노드가 존재할 때까지만 반복
                left = curr * 2
                right = curr * 2 + 1
                smallest = curr # 우선 내가 제일 작다고 가정
                
                # 왼쪽 자식이 나보다 작다면 최소 노드 변경
                if self.heap[left] < self.heap[smallest]: 
                    smallest = left
                # 오른쪽 자식이 현재 최소 노드보다 더 작다면 최소 노드 변경
                if right < len(self.heap) and self.heap[right] < self.heap[smallest]: 
                    smallest = right
                # 자식들이 나보다 크다면 제자리를 찾은 것이므로 종료
                if smallest == curr: 
                    break
                    
                # 나보다 작은 자식과 자리를 교체
                self.heap[curr], self.heap[smallest] = self.heap[smallest], self.heap[curr]
                curr = smallest # 바늘을 내려간 자식 위치로 이동
        return min_val

    #  현재 힙에 데이터가 몇 개 쌓여있는지 알려줌
    def size(self):
        return len(self.heap) - 1

# 허프만 트리
def make_tree(freq):
    heap = MinHeap()
    
    # 빈도수 리스트의 모든 데이터를 최소 힙에 삽입
    for n in freq:
        heap.insert(n)
    # 힙 속에 데이터가 단 1개(최종 루트 노드) 남을 때까지 무한 반복
    while heap.size() > 1:
        e1 = heap.delete()  # 힙에서 가장 작은 빈도수를 가진 노드 꺼냄
        e2 = heap.delete()  # 그다음으로 작은 빈도수를 가진 노드 꺼냄
        
        # 두 자식 노드를 합친 새로운 부모 노드(e1 + e2)를 만들어 다시 힙에 넣음
        heap.insert(e1 + e2)
        
        # 결합되는 과정 출력
        print(" (%d+%d)" % (e1, e2))
        
label = [ 'E', 'T', 'N', 'I', 'S' ]
freq  = [ 15, 12, 8, 6, 4 ]

# 트리 조립 함수 실행
make_tree(freq)