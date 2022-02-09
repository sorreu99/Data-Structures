class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        if not self.items:
            return True

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Empty stack")


s = Stack()
print(s.peek())
print(s.get_stack())
s.is_empty()
s.push(20)
print(s.get_stack())
s.pop()
print(s.get_stack())
