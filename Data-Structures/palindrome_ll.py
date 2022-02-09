class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_palindrome(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        if temp.data != stack.pop():
            print("Not a palindrome")
            return
        else:
            temp = temp.next
    print("It is a Palindrome")


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


def pairwise_swap(head):
    temp = head
    while True:
        if temp is None or temp.next is None:
            return
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next


def create_intersection_ll(head1, head2):
    temp1 = head1
    head3 = None
    while temp1:
        temp2 = head2
        # print("temp1 data:")
        # print(temp1.data)
        while temp2:
            # print("temp2 data:")
            # print(temp2.data)
            if temp1.data == temp2.data:
                if head3 is None:
                    head3 = Node(temp1.data)
                    break
                else:
                    insert_at_last(head3, temp1.data)
            temp2 = temp2.next
        temp1 = temp1.next
    # print(head3.data)
    return head3


head1 = Node(1)
insert_at_last(head1, 2)
insert_at_last(head1, 3)
insert_at_last(head1, 4)
insert_at_last(head1, 6)

# head2 = Node(2)
# insert_at_last(head2, 4)
# insert_at_last(head2, 6)
# insert_at_last(head2, 8)

# is_palindrome(head)
# print("before")
# view_list(head)
# print("after swap")
# pairwise_swap(head)
# view_list(head)
# print("after removing the duplicates")
# remove_duplicates(head)
# view_list(head)
# print("after pairwise swap")
# pairwise_swap(head)
# view_list(head)
# head3 = create_intersection_ll(head1, head2)
# view_list(head3)


