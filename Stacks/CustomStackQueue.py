class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
    def __repr__(self) -> str:
        return str(self.val)
    def __str__(self) -> str:
        return str(self.val)

class Queue:
    def __init__(self, *values):
        self.head = None
        self.tail = None
        for val in values:
            self.append(val)

    def append(self, value):
        node=Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        if not self.head:
            raise IndexError("Queue is empty")
        else:
            poped = self.head
            self.head = self.head.next
            if poped == self.tail:
                self.tail = None
            return poped
        
    def __repr__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr))
            curr = curr.next

        return '<->'.join(values)
    
class Stack:
    def __init__(self, *values):
        self.head = None
        for val in values:
            self.push(val)

    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def pop(self):
        if not self.head:
            raise IndexError("Stack is empty")
        else:
            popped = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return popped
        
    def __repr__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr))
            curr = curr.next

        return ' <- '.join(values)

print("<------queue--------->")

q1 = Queue(1) 
print(q1)
q1.append(2)
q1.append(3)
print(q1)
print(q1.pop()) #first in:1 first out
print(q1.pop()) #first in:2 first out
print(q1) #3

print("<-----stack------>")

s = Stack(1)
print(s)
s.push(2)
s.push(3)
print(s)
print(s.pop()) #Last in:3 first out
print(s.pop()) #Last in:2 first out
print(s) #1