class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_odd_levels(node):
    stack = []
    if node == None:
        return
    stack.append(node.data)
    print_odd_levels(node)

