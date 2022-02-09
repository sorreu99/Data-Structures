import class_node


class LinkedList:  # creating a class for linked list having all the methods required for its operation

    def __init__(self):
        self.head = None

    def insert_last(self, value):

        new_node = class_node.Node(value)
        if head is None:
            head = new_node

        else:
            temp = head
            while (temp.next != None):
                temp = temp.next
            temp.data = value

    def view_list():
        global head
        if head is None:
            print("linked list is empty")
        else:
            temp1 = head
            while (temp1.next != None):
                print(temp1.data)
