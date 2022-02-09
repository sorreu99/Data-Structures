class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_sum_children(node):
    left_data = 0
    right_data = 0
    if node == None or (node.left == None and node.right == None):
        return 1
    if node.left:
        left_data = node.left.data
    if node.right:
        right_data = node.right.data
    if node.data == left_data + right_data and is_sum_children(node.right) and is_sum_children(node.left):
        return 1
    else:
        return 0


node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.right.left = Node(6)
node.right.right = Node(2)

if is_sum_children(node):
    print("sum of children is equal to the node")
else:
    print("sum not equal to the node")
