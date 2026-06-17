class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None   
        self.right = None  

class BinarySearchTree:
    def __init__(self):
        self.root = None  # 트리의 시작점

    # 탐색 연산
    def search(self, key):
        curr = self.root 
        
        while curr is not None:
            if curr.data == key:
                return curr  # 찾으면 해당 노드를 반환
            elif curr.data > key:
                curr = curr.left  # 찾으려는 값이 더 작으면 왼쪽으로 이동
            else:
                curr = curr.right # 찾으려는 값이 더 크면 오른쪽으로 이동
                
        return None  # 없으면 None 반환

    # 삽입 연산
    def insert(self, data):
        new_node = TreeNode(data)
        
        # 트리가 비어있으면 새 노드가 바로 루트가 됨
        if self.root is None:
            self.root = new_node
            return

        curr = self.root
        while True:
            # 현재 노드보다 넣으려는 값이 작다면 왼쪽으로 이동
            if curr.data > data:
                if curr.left is None: # 왼쪽이 비어있다면 여기에 삽입
                    curr.left = new_node
                    break
                curr = curr.left
            # 현재 노드보다 넣으려는 값이 크다면 오른쪽으로 이동
            else:
                if curr.right is None: # 오른쪽이 비어있다면 여기에 삽입
                    curr.right = new_node
                    break
                curr = curr.right
        print(f"-> {data} 삽입 완료!")

    # 삭제 연산
    # 삭제는 직접 노드를 끊어함 -> 재귀 구조 사용
    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, curr, key):
        if curr is None: return None

        # 삭제할 노드를 찾으러 내려감
        if key < curr.data:
            curr.left = self._delete_node(curr.left, key)
        elif key > curr.data:
            curr.right = self._delete_node(curr.right, key)
            
        # 삭제할 노드(curr)를 찾아냈을 때 처리
        else:
            # 자식이 없거나 1개만 있는 경우
            if curr.left is None:
                return curr.right # 오른쪽 자식을 현재 자리에 넣고 현재 위치 값은 없어짐
            elif curr.right is None:
                return curr.left  # 왼쪽 자식을 현재 자리에 넣고 현재 위치 값은 없어짐

            # 자식이 양쪽에 다 있는 경우
            # 오른쪽 자식들 중에서 가장 작은 값을 가진 노드를 찾아옴
            succ = curr.right
            while succ.left is not None:
                succ = succ.left
                
            # 현재 자리에 그 노드의 데이터를 복사해옴
            curr.data = succ.data
            # 데이터를 받아왔으니 오른쪽 아래에 남아있는 중복된 노드 삭제
            curr.right = self._delete_node(curr.right, succ.data)

        return curr

    # 중위 순회
    def inorder(self, curr):
        if curr is not None:
            self.inorder(curr.left)
            print(curr.data, end=" ")
            self.inorder(curr.right)


# --- 테스트 코드 ---
bst = BinarySearchTree()

print("--- 데이터 삽입 ---")
bst.insert(30)
bst.insert(15)
bst.insert(45)
bst.insert(10)
bst.insert(20)

print("\n--- 정렬 검증---")
bst.inorder(bst.root) # 출력: 10 15 20 30 45
print("\n")

print("--- 탐색 테스트 ---")
target = 20
found = bst.search(target)
if found:
    print(f"값 {target}을 찾았습니다")
else:
    print(f"값 {target}이 트리에 없습니다")

print("\n--- 삭제 테스트 ---")
bst.delete(15)
print("삭제 후 트리 상태:")
bst.inorder(bst.root) # 15가 지워지고 그 자리에 20이 채워져서 [10 20 30 45] 형태로 정렬 유지됨
print()