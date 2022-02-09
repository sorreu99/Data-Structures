from node_bst import Node


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def insert_node(self, data):
        temp = self.root

        while True:
            if data >= temp.data:
                if temp.right is None:
                    temp.right = Node(data)
                    break

                temp = temp.right

            elif data < temp.data:
                if temp.left is None:
                    temp.left = Node(data)
                    break

                temp = temp.left

    def view_in_order(self):
        stack = []
        temp = self.root
        while True:
            if temp is not None:
                stack.append(temp)
                temp = temp.left

            elif stack:
                temp = stack.pop()
                print(temp.data)
                temp = temp.right

            else:
                return

    def view_pre_order(self):
        stack = []
        temp = self.root
        while True:
            if temp:
                print(temp.data)
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    temp = temp.left
                elif stack:
                    temp = stack.pop()
                else:
                    break

    def view_post_order(self):
        stack = [self.root]
        prev = None

        while True:

            current = stack[-1]
            if prev is None or prev.left is current or prev.right is current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    stack.pop()
                    print(current.data)

            elif current.left is prev:
                if current.right:
                    stack.append(current.right)
                else:
                    stack.pop()
                    print(current.data)
            elif current.right is prev:
                stack.pop()
                print(current.data)

            prev = current

            if not stack:
                break

    def delete_node(self, key):
        current_left = None
        current_right = None
        temp = self.root
        while temp.data != key:
            if temp.data > key:
                prev = temp
                temp = temp.left
            else:
                prev = temp
                temp = temp.right
            if temp is None:
                print("The key not found in the tree")
                return
        if temp.left:
            current_left = temp.left
        if temp.right:
            current_right = temp.right
        # if the node itself is a child node

        if temp.left is None and temp.right is None:
            if prev.data > temp.data:
                prev.left = None
            else:
                prev.right = None

        # if th node has no left node but only 1 child node at right side
        elif temp.left is None and temp.right.right is None and temp.right.left is None:
            if prev.data > temp.data:
                prev.left = temp.right


            else:
                prev.right = temp.right

        # if the node has only 1 child on left side
        elif temp.left.left is None and temp.left.right is None:

            if temp.right:
                if prev.data > temp.data:
                    prev.left = temp.left
                    prev.left.right = current_right

                else:
                    prev.right = temp.left
                    prev.right.right = current_right

            elif prev.data > temp.data:
                prev.left = temp.left
            else:
                prev.right = temp.left

        elif temp.left:  # if the node has left subtree we will traverse left
            prev_replace = temp
            temp = temp.left
            while temp.right:  # In the left subtree, we will find the largest number
                prev_replace = temp
                temp = temp.right
            if prev.data > temp.data:
                if temp.data > prev_replace.data:

                    prev.left = prev_replace.right
                    prev_replace.right = None
                else:
                    prev.left = prev_replace.left
                    prev_replace.left = None
                prev.left.left = current_left
                prev.left.right = current_right

            elif temp.data > prev_replace.data:
                prev.right = prev_replace.right
                prev_replace.right = None
                prev.right.left = current_left
                prev.right.right = current_right
            else:
                prev.right = prev_replace.left
                prev_replace.left = None
                prev.right.left = current_left
                prev.right.right = current_right

        # if the node does not have left subtree we will traverse right and find the smallest number

        elif temp.right:
            prev_replace = temp
            temp = temp.right
            while temp.left:
                prev_replace = temp
                temp = temp.left
            if prev.data > temp.data:
                if temp.data > prev_replace.data:
                    prev.left = prev_replace.right
                    prev.left.left = current_left
                    prev.left.right = current_right
                    prev_replace.right = None
                else:
                    prev.left = prev_replace.left
                    prev.left.left = current_left
                    prev.left.right = current_right
                    prev_replace.left = None

            else:
                if temp.data > prev_replace.data:
                    prev.right = prev_replace.right
                    prev.right.left = current_left
                    prev.right.right = current_right
                    prev_replace.right = None
                else:
                    prev.right = prev_replace.left
                    prev.right.left = current_left
                    prev.right.right = current_right
                    prev_replace.left = None

    def level_order_traverse(self):

        queue = [self.root]
        while True:
            if queue:
                temp = queue.pop(0)
            else:
                return
            print(temp.data)

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)








