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


def segregate_even_odd(head):
    flag = 0
    temp = head
    while temp:
        last = temp
        temp = temp.next
    temp = head
    while temp != last:
        if temp.data % 2 == 1:
            current = temp
            while current.next:
                current = current.next
            if temp != head:
                nxt = temp.next
                prev.next = nxt
                current.next = temp
                temp.next = None

            else:
                current.next = temp
                nxt = temp.next
                temp.next = None
            temp = nxt
            if flag == 0:
                head = temp



        else:
            if flag == 0:
                head = temp
            prev = temp
            temp = temp.next
            flag = 1

    if temp.data % 2 == 1:
        current = temp
        while current.next:
            current = current.next
        nxt = temp.next
        temp.next = None
        prev.next = nxt
        current.next = temp

    return head


head = Node(17)
insert_at_last(head, 15)
insert_at_last(head, 10)
insert_at_last(head, 12)
insert_at_last(head, 4)
insert_at_last(head, 1)
insert_at_last(head, 7)
print("before segregation")
view_list(head)
new_head = segregate_even_odd(head)
print("after segregation")
view_list(new_head)
