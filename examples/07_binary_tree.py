from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(node):
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]


def level_order(root):
    if root is None:
        return []

    result = []
    q = deque([root])

    while q:
        node = q.popleft()
        result.append(node.data)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return result


if __name__ == "__main__":
    root = Node("A",
                Node("B", Node("D"), Node("E")),
                Node("C"))

    print("전위:", preorder(root))
    print("중위:", inorder(root))
    print("후위:", postorder(root))
    print("레벨:", level_order(root))
