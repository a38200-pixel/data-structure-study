class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class InsertionSortList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    # 삽입 정렬 함수
    def insertion_sort(self):
        # 임시 head 생성
        sorted_head = None
        
        curr = self.head  # 원본 리스트를 처음부터 쭉 훑고 지나갈 노드
        while curr is not None:
            next_node = curr.next  # 다음 턴에 볼 노드를 미리 저장해둠
            
            # 정렬된 리스트(sorted_head)의 맨 앞에 들어갈 수 있는지 확인
            if sorted_head is None or sorted_head.data >= curr.data:
                curr.next = sorted_head
                sorted_head = curr
            else:
                # 정렬된 리스트의 중간이나 끝에 적절한 위치를 찾아 들어감
                search = sorted_head
                while search.next is not None and search.next.data < curr.data:
                    search = search.next
                
                # 찾은 위치 사이에 끼워 넣기
                curr.next = search.next
                search.next = curr
                
            curr = next_node  # 미리 챙겨둔 다음 노드로 이동
            
        self.head = sorted_head  # 정렬 완료된 리스트로 교체

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# --- 테스트 코드 ---
sll = InsertionSortList()
sll.append(40)
sll.append(10)
sll.append(30)
sll.append(20)

print("정렬 전:")
sll.display() # 40 -> 10 -> 30 -> 20 -> None

print("\n삽입 정렬 실행 후:")
sll.insertion_sort()
sll.display() # 10 -> 20 -> 30 -> 40 -> None