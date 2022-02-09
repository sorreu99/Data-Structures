class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_loop(head):
    slow = head
    fast = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            print("The linked list is in loop")
            return
    print("Not in loop")

def detect_count_loop(head):
    slow = head
    fast = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            print("The linked list is in loop")
            slow = slow.next
            fast = fast.next.next
            count = 1
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
                count = count + 1
            return  count
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next
print(detect_count_loop(head))
