from collections import deque
class Stack:
    def __init__(self):
        self.s = deque()
    def pop(self):
        return self.s.pop()
    def push(self,value):
        self.s.append(value)
    def pull(self):
        return self.s[-1]
    def isEmpty(self):
        if self.s == []:
            return True

        return False
    def size(self):
        return len(s)

    def print(self):
        print(self.s)
        return


a = Stack()
a.push(5)
a.push(6)
a.print()
a.pop()
a.print()