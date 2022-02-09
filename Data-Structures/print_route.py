class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


stack = []


def print_route(stack, node):
    if node == None:
        return 0
    stack.append(node.data)
    if node.left == None and node.right == None:
        print(stack)
    print_route(stack, node.left)
    print_route(stack, node.right)
    stack.pop()


node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.right = Node(50)
node.left.left = Node(5)
node.left.left.right = Node(10)
node.right.left = Node(4)
node.right.right = Node(8)
node.right.right.left = Node(6)
print_route(stack, node)