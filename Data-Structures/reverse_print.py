class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_last(head, data):
    if head is None:
        head = Node(data)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)


def view_list(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


def print_reverse(head, prev=None):
    temp = head
    if temp == prev:
        return
    while temp.next != prev:
        temp = temp.next
    prev = temp
    print(temp.data)
    print_reverse(head, prev)


head = Node(1)
insert_at_last(head, 2)
insert_at_last(head, 3)
insert_at_last(head, 4)
insert_at_last(head, 5)
print("Forward printing")
view_list(head)
print("Reverse printing")
print_reverse(head)


