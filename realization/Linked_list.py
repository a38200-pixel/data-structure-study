class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드를 가리키는 포인터

class SimpleLinkedList:
    def __init__(self):
        self.head = None  # 시작점

    # 맨 뒤에 데이터 추가 (Append)
    def append(self, e):
        new_node = Node(e)
        
        # 비어있다면 새 노드가 head가 됨
        if self.head is None:
            self.head = new_node  
        else:
            # 맨 끝 칸을 찾을 때까지 이동
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            # 가장 마지막 칸 뒤에 새 노드를 연결
            curr.next = new_node  

    # 리스트 전체 출력
    def display(self):
        print("연결된 구조 리스트: [", end="")
        curr = self.head
        while curr is not None:
            print(curr.data, end=", " if curr.next is not None else "")
            curr = curr.next 
        print("]")

# --- 테스트 ---
lnk_list = SimpleLinkedList()
lnk_list.append(10)
lnk_list.append(20)
lnk_list.append(30)

lnk_list.display()  # 출력: [10, 20, 30]