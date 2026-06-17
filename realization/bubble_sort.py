class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class BubbleSortLinkedList:
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

    # 버블 정렬 함수
    def bubble_sort(self):
        if self.head is None:
            return

        # 정렬이 완료된 뒤쪽 구역을 한 칸씩 당겨서 제한하는 역할
        end_node = None

        # end_node이 첫 번째 노드(head)까지 올 때까지 반복
        while end_node != self.head:
            curr = self.head  # 새 턴이 시작될 때마다 맨 앞으로 돌아감
            
            # 바로 옆 칸 = curr.next, 정렬 완료된 곳 직전까지감
            while curr.next != end_node:
                next_node = curr.next
                
                # 현재 노드의 값이 오른쪽 노드의 값보다 크다면?
                if curr.data > next_node.data:
                    # 두 노드의 데이터를 바꿈
                    curr.data, next_node.data = next_node.data, curr.data
                
                curr = curr.next  # 다음 칸으로 이동
                
            # 한 바퀴 다 돌았으면 끝
            end_node = curr 

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# --- 테스트 코드 ---
test = BubbleSortLinkedList()

print("--- 데이터 추가 ---")
test.append(50)
test.append(20)
test.append(40)
test.append(10)
test.display()  # 출력: 50 -> 20 -> 40 -> 10 -> None

print("\n--- 버블 정렬 실행 ---")
test.bubble_sort()
test.display()  # 출력: 10 -> 20 -> 40 -> 50 -> None