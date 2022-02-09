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


def reverse_ll(head):
    prev = None
    temp = head
    while temp:
        next_temp = temp.next
        temp.next = prev
        prev = temp
        temp = next_temp
    return prev


head = Node(1)
insert_at_last(head, 2)
insert_at_last(head, 3)
insert_at_last(head, 4)
insert_at_last(head, 5)
print("Before reversing")
view_list(head)
print("After reversing")
new_head_returned = reverse_ll(head)
view_list(new_head_returned)
