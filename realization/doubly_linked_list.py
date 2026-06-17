class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # 이전 노드를 가리킴
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:  # 맨 끝 노드를 찾음
                curr = curr.next
            
            # 찾은 마지막 노드와 새 노드를 연결
            curr.next = new_node          # 앞 노드가 새 노드를 가리킴
            new_node.prev = curr          # 새 노드도 앞 노드를 가리킴

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

# 리스트 객체 생성 및 데이터 추가
test = DoublyLinkedList()
print("--- Append ---")
test.append(10)
test.append(20)
test.append(30)

# 정방향 출력
print("\n--- 정방향 출력 (next 확인) ---")
test.display()  # 출력: 10 <-> 20 <-> 30 <-> None


# 역방향 출력
print("\n--- 역방향 출력 (prev 확인) ---")
# 가장 마지막 노드인 30까지 이동
curr = test.head
while curr.next is not None:
    curr = curr.next

print("None", end="")
while curr is not None:
    print(f" <-> {curr.data}", end="")
    curr = curr.prev  # 역방향으로 이동
print("시작점")