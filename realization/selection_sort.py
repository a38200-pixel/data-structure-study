class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SelectionSortList:
    def __init__(self):
        self.head = None

    # 데이터 추가
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    # 선택 정렬 함수
    def selection_sort(self):
        if self.head is None:
            return

        # i_node = 기준 자리
        i_node = self.head
        while i_node.next is not None:
            
            # i_node부터 끝까지 중 가장 작은 값을 가진 노드를 찾음
            least_node = i_node
            j_node = i_node.next
            
            while j_node is not None:
                if j_node.data < least_node.data:
                    least_node = j_node  # 최솟값 노드 업데이트
                j_node = j_node.next     # 다음 노드로 이동
            
            # 찾은 최솟값(least_node.data)과 기준 자리(i_node.data)의 값을 바꿈
            i_node.data, least_node.data = least_node.data, i_node.data
            
            i_node = i_node.next # 다음 기준 자리로 이동

    # 출력 함수
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# --- 테스트 코드 ---
sll = SelectionSortList()

print("데이터 추가")
sll.append(30)
sll.append(10)
sll.append(40)
sll.append(20)
sll.display() # 출력 = 30 -> 10 -> 40 -> 20 -> None

print("선택 정렬 실행")
sll.selection_sort()
sll.display() # 출력 = 10 -> 20 -> 30 -> 40 -> None