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


def remove_duplicates(head):
    temp = head
    while temp.next:
        prev = temp.next
        if temp.data == prev.data:
            temp.next = prev.next
        while prev.next:
            if temp.data == prev.next.data:
                prev.next = prev.next.next
            prev = prev.next

        temp = temp.next



