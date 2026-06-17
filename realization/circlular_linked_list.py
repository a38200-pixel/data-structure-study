class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None  # head 대신 tail
        self.size = 0

    # 맨 뒤에 데이터 추가
    def append(self, data):
        new_node = Node(data)
        
        # 리스트가 텅 비어있을 때
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node  # 원형이라 자기 자신을 가리킴
        # 이미 데이터가 있을 때
        else:
            new_node.next = self.tail.next  # 새 노드가 기존 head를 가리킴
            self.tail.next = new_node        # 기존 tail이 새 노드를 가리킴
            self.tail = new_node             # 이제 새 노드가 새로운 tail이 됨
            
        self.size += 1

    # 리스트의 모든 데이터 출력하기
    def display(self):
        if self.tail is None:
            print("Empty List")
            return
        
        curr = self.tail.next  # tail.next가 head
        for _ in range(self.size):
            print(curr.data, end=" -> ")
            curr = curr.next
        print("처음으로 돌아옴 (tail)")

test = CircularLinkedList()

print("테스트")
test.append(10)  # 10 -> 10
test.append(20)  # 10 -> 20 -> 10
test.append(30)  # 10 -> 20 -> 30 -> 10
test.display()