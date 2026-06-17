class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None   # 왼쪽 자식 노드를 가리키는 포인터
        self.right = None  # 오른쪽 자식 노드를 가리키는 포인터

class BinaryTree:
    def __init__(self):
        self.root = None

    # 전위 순회 : 루트 -> 왼쪽 -> 오른쪽
    def preorder(self, curr):
        if curr is not None:
            print(curr.data, end=" ")    # 현재 노드
            self.preorder(curr.left)     # 왼쪽 자식으로 이동
            self.preorder(curr.right)    # 오른쪽 자식으로 이동

    # 중위 순회 : 왼쪽 -> 루트 -> 오른쪽
    def inorder(self, curr):
        if curr is not None:
            self.inorder(curr.left)      # 왼쪽 자식으로 이동
            print(curr.data, end=" ")    # 현재 노드
            self.inorder(curr.right)     # 오른쪽 자식으로 이동

    # 후위 순회 : 왼쪽 -> 오른쪽 -> 루트
    def postorder(self, curr):
        if curr is not None:
            self.postorder(curr.left)    # 왼쪽 자식으로 이동
            self.postorder(curr.right)   # 오른쪽 자식으로 이동
            print(curr.data, end=" ")    # 현재 노드


# --- 테스트 코드 ---
tree = BinaryTree()

# 노드 생성
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")

# 노드 연결 (트리 조립)
tree.root = nodeA
nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE

print("--- 전위 순회 ---")
# 시작 노드인 tree.root를 curr 매개변수로 전달합니다.
tree.preorder(tree.root)   # 출력: A B D E C
print("\n")

print("--- 중위 순회 ---")
tree.inorder(tree.root)    # 출력: D B E A C
print("\n")

print("--- 후위 순회 ---")
tree.postorder(tree.root)  # 출력: D E B C A
print()