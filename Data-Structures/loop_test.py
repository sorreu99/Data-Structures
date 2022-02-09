class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = None
    def insert_node(self, data):
        if head is None:
            head = Node(data)
        else:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    def view_list(self):
        if head is None:
            print("list is empty")
        else:
            temp = head
            while temp:
                print(temp.data)
                temp = temp.next
ll1 = LinkedList()
ll1.insert_node(1)
ll1.view_list()






