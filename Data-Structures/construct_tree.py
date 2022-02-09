class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

in_order_list = ["D", "B", "E", "A", "F", "C"]
pre_order_list = ["A", "B","D", "E", "C", "F"]

def search_index(key, list):
    index = 0
    for i in list:
        if i == key:
            return index
        index = index + 1
        if index == len(list):
            print("Key not in the list.")
            return


def construct_tree(in_order_list, pre_order_list):
    root = Node(pre_order_list.pop(0))
    temp = root
    lowest = in_order_list[0]

    #  going to the extreme left of the tree till the lowest number
    for i in range(search_index(lowest, pre_order_list) + 1):
        temp.left = Node(pre_order_list.pop(0))
        temp = temp.left










construct_tree(in_order_list, pre_order_list)

