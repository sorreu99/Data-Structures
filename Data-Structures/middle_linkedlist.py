class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def middle_ll(head):
    slow = head
    fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast.next.next == None:
            break
    print(slow.data)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

middle_ll(head)
