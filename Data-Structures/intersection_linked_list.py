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


def intersection(head1, head2):
    stack1 = []
    stack2 = []
    temp1 = head1
    temp2 = head2
    while temp1:
        stack1.append(temp1)
        temp1 = temp1.next

    while temp2:
        stack2.append(temp2)
        temp2 = temp2.next

    for i in stack1:
        for j in stack2:
            if i == j:
                print("linked lists are intersecting at", i.data)
                return
    print("Not intersecting")








head1 = Node(1)
head2 = Node(5)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head2.next = Node(6)
head2.next.next = Node(7)
head2.next.next.next = head1.next.next
intersection(head1, head2)
