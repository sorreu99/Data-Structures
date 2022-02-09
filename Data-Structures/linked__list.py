from node import Node


class LinkedList:  # creating a class for linked list having all the methods required for its operation

    def __init__(self):
        self.head = None

    def insert_last(self, value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.data = value


        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def view_list(self):  # to print the data stored in the linked list

        if self.head is None:
            print("linked list is empty")
        else:
            temp1 = self.head
            while (temp1 != None):
                print(temp1.data)
                temp1 = temp1.next

    def length_ll(self):  # to find the length of linked list
        count = 0
        temp = self.head
        while (temp != None):
            count += 1
            temp = temp.next
        return count

    def get_at_index(self, index):  # to get the value at a particular index number

        if index > self.length_ll() or index < 1:
            return "Error: Index out of range!"
        else:
            count = 1
            temp = self.head
            while True:
                if count == index:
                    return "The value at " + str(index) + " index is " + str(temp.data)
                count += 1
                temp = temp.next

    def delete_node(self, index):

        if self.head is None:
            print("list is already empty")

        if index > self.length_ll() or index < 1:

            print("Error : out of index range")

        else:

            count = 1

            if count == index:  # if the head is referring to the node which we want to delete
                self.head = self.head.next

            else:

                temp = self.head

                while True:

                    last_node = temp

                    temp = temp.next

                    if count == index - 1:
                        last_node.next = temp.next

                        return

                    count += 1

    def insert_at_index(self, index, value):  # insert a node at given index

        if index > self.length_ll() or index < 1:
            print("Error: Index out of range!")
        new_node = Node(value)
        count = 1
        if index == 1:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            return
        temp = self.head

        while True:
            last_node = temp
            temp = temp.next
            if count == index - 1:
                last_node.next = new_node
                new_node.next = temp

                return

            count += 1

    def reverse_ll(self):  # reverse the complete linked list

        if self.length_ll() == 0:
            print("Empty list")

        else:
            temp = self.head
            prev = None

            while temp.next is not None:
                nxt = temp.next
                temp.next = prev
                prev = temp

                temp = nxt
            temp.next = prev
            self.head = temp

        self.view_list()

    def sorting_ll(self):  # Sorting the linked list in the increasing order.

        for i in range(self.length_ll() - 1):
            print("start: ")
            self.view_list()
            prev = None
            temp = self.head
            for j in range(self.length_ll() - i - 1):
                if temp.data > temp.next.data:
                    if temp == self.head:

                        self.head = temp.next
                        temp.next = temp.next.next
                        self.head.next = temp
                        prev = self.head
                        self.view_list()

                    else:
                        prev_next = prev.next
                        prev.next = temp.next

                        temp.next = temp.next.next
                        prev.next.next = prev_next
                        prev = prev.next
                else:
                    prev = temp
                    temp = temp.next

        print("final: ")
        self.view_list()
