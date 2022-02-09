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


def last_element_at_first(head):
    temp = head
    prev = None
    while temp.next:
        prev = temp
        temp = temp.next
    prev.next = None
    temp.next = head
    new_head = temp
    return new_head


head = Node(1)
insert_at_last(head, 2)
insert_at_last(head, 3)
insert_at_last(head, 4)

new_head = last_element_at_first(head)
view_list(new_head)
