class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1 

class AVLTree:
    def __init__(self):
        self.root = None

    # 노드의 높이 (None인 자식은 높이가 0)
    def _get_height(self, node):
        if node is None: return 0
        return node.height

    # 왼쪽과 오른쪽의 높이 차이(균형 인수)를 계산하는 함수
    def _get_balance(self, node):
        if node is None: return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # 오른쪽으로 회전
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # 회전 수행
        x.right = y
        y.left = T2

        # 회전 후 노드들의 높이 갱신
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1

        return x  # 새로운 루트 노드 반환

    # 왼쪽으로 회전
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # 회전 수행
        y.left = x
        x.right = T2

        # 회전 후 노드들의 높이 갱신
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        return y  # 새로운 루트 노드 반환

    # 삽입 연산 외부 호출
    def insert(self, data):
        self.root = self._insert_node(self.root, data)
        print(f"-> {data} 삽입 및 균형 정렬 완료")

    # 실제 삽입을 수행하는 내부 재귀 함수
    def _insert_node(self, curr, data):
        # 일반 이진 탐색 트리와 똑같이 자리를 찾아 내려가며 삽입
        if curr is None:
            return Node(data)

        if data < curr.data:
            curr.left = self._insert_node(curr.left, data)
        elif data > curr.data:
            curr.right = self._insert_node(curr.right, data)
        else:
            return curr  # 중복된 데이터는 허용하지 않음

        # 자식이 들어왔으니 현재 노드(curr)의 높이를 업데이트
        curr.height = max(self._get_height(curr.left), self._get_height(curr.right)) + 1

        # 왼쪽과 오른쪽이 얼마나 쏠렸는지 균형 수치를 구함
        balance = self._get_balance(curr)

        # 만약 균형이 깨졌다면(수치가 > 1 또는 < -1), 4가지 상황에 맞춰 회전함

        # 경우 1: LL 상태 (왼쪽 자식의 왼쪽에 추가됨) -> 오른쪽으로 1번 회전
        if balance > 1 and data < curr.left.data:
            return self._rotate_right(curr)

        # 경우 2: RR 상태 (오른쪽 자식의 오른쪽에 추가됨) -> 왼쪽으로 1번 회전
        if balance < -1 and data > curr.right.data:
            return self._rotate_left(curr)

        # 경우 3: LR 상태 (왼쪽 자식의 오른쪽에 추가됨) -> 왼쪽 회전 후 오른쪽 회전
        if balance > 1 and data > curr.left.data:
            curr.left = self._rotate_left(curr.left)
            return self._rotate_right(curr)

        # 경우 4: RL 상태 (오른쪽 자식의 왼쪽에 추가됨) -> 오른쪽 회전 후 왼쪽 회전
        if balance < -1 and data < curr.right.data:
            curr.right = self._rotate_right(curr.right)
            return self._rotate_left(curr)

        return curr

    # 전위 순회
    def preorder(self, curr):
        if curr is not None:
            print(curr.data, end=" ")
            self.preorder(curr.left)
            self.preorder(curr.right)


# --- 테스트 코드 ---
avl = AVLTree()

print("--- 테스트 ---")
avl.insert(10)
avl.insert(20)
avl.insert(30)

print("\n--- 전위 순회 결과 (Root -> L -> R) ---")
avl.preorder(avl.root) 
print()