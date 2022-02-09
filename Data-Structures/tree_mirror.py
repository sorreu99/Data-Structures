class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_mirror(node1, node2):
    print('{0}, {1}'.format(node1.data if node1 else 'None', node2.data if node2 else 'None'))

    if node1 is None and node2 is None:
        return 1
    if node1 is None or node2 is None:
        return 0
    if node1.data != node2.data:
        return 0

    print('Into left subtree')
    left_mirror = is_mirror(node1.left, node2.right)

    print('Into right subtree')
    right_mirror = is_mirror(node1.right, node2.left)

    if node1.data == node2.data and left_mirror and right_mirror:
        return 1
    else:
        return 0


node1 = Node(2)
node2 = Node(2)
node1.left = Node(8)
node2.right = Node(8)
node1.right = Node(6)
node2.left = Node(6)
node1.right.left = Node(5)
node2.left.right = Node(5)
node1.right.right = Node(3)
node2.left.left = Node(3)

if is_mirror(node1, node2):
    print("Both trees are mirror of each other")
else:
    print("Not mirror images")
