class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 맨 앞에 노드 삽입하기
    def insert_front(self, data):
        new_node = Node(data)      # 새로운 노드 생성
        new_node.next = self.head  # 새 노드가 기존의 첫 번째 노드를 가리키게 함
        self.head = new_node       # 이제 새 노드가 시작점(head)이 됨

    # 맨 앞의 노드 삭제하기
    def delete_front(self):
        if self.head is None:      # 리스트가 비어있다면 삭제 불가
            return None
        
        removed_data = self.head.data  # 삭제할 노드의 데이터를 백업
        self.head = self.head.next     # head를 두 번째 노드로 한 칸 이동시킴
        return removed_data            # 삭제된 데이터 반환

    # 리스트의 모든 데이터 출력하기
    def display(self):
        curr = self.head           # 시작점부터 탐색 출발
        while curr is not None:    # 다음 노드가 없을 때까지 반복
            print(curr.data, end=" -> ")
            curr = curr.next       # 다음 노드로 이동
        print("None")

test = SinglyLinkedList()

print("맨 앞에 10, 20, 30을 차례대로 삽입")
test.insert_front(10) # 10 -> None
test.insert_front(20) # 20 -> 10 -> None
test.insert_front(30) # 30 -> 20 -> 10 -> None
test.display()

print("맨 앞 노드(30) 하나 삭제")
deleted_val = test.delete_front()
print(f"삭제된 데이터: {deleted_val}")
test.display()