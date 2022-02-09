from binary_tree import BinaryTree
b = BinaryTree(3)
try:
    b.insert_node(5)
except Exception:
    print("error with the parameter passed")
b.insert_node(4)
b.insert_node(2)
b.insert_node(1)
b.insert_node(2.5)
b.insert_node(1.5)
print("After inserting all the nodes, traverse using post order ")
b.view_post_order()
print("deleting a node\n")
b.delete_node(10)
print("After deleting traversing the nodes using post order traverse")
b.view_post_order()
print("Level order traverse")
b.level_order_traverse()
