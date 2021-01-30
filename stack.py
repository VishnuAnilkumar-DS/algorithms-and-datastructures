class Stack:
    def __init__(self):
        self.stack = []  # one dir array (abstract datatype)

    # push method or insertion // O(1)
    def push(self, data):
        self.stack.append(data)

    # moving item In LIFO way ie pop first element // O(1)
    def pop(self):
        if self.stack_size() < 1:
            return -1
        data = self.stack.pop(-1)
        return data

    # peek or view last element in stack without remove removing it // O(1)
    def peek(self):
        return self.stack[-1]

    # checks whether empty or not // O(1)
    def is_empty(self):
        return self.stack == []

    # return size of stack //O(1)
    def stack_size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("size of stack %d" % stack.stack_size())
print("Popped item %d" % stack.pop())
print("size of stack %d" % stack.stack_size())
print("Peek item %d" % stack.peek())
print("size of stack %d" % stack.stack_size())
