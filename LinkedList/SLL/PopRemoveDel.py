class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, *values):
        self.head = None
        self.tail = None
        self.length = 0
        for value in values:
            self.append(value)

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(nodes) + ' -> None'

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        """
        Removes the last node from the linked list and returns its value.
        
        Raises
        ------
        BufferError
            If the linked list is empty.
        
        Returns
        -------
        any
            The value of the removed node.
        """
        if not self.head:
            raise BufferError("No element found in Linked List")

        if self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None
        self.tail = current
        self.length -= 1
        return value
    
    def remove(self, index: int):
        """
        Removes the node at the given index.
        
        Parameters
        ----------
        index : int
            The index of the node to remove. Must be a non-negative integer.
        
        Raises
        ------
        IndexError
            If the index is out of range (index < 0 or index >= length of the linked list)
        BufferError
            If the linked list is empty.
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if self.length == 0:
            raise BufferError("Linked List is empty")

        if index == 0:
            self.head = self.head.next
            if self.length == 1:  # If it was the only element
                self.tail = None
            self.length -= 1
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        removed_node = current.next
        current.next = removed_node.next

        if index == self.length - 1:  # If the removed node is the last node
            self.tail = current

        self.length -= 1
        return

    def delete(self):
        """
        delete all the nodes of Linked List
        """
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = None
            curr = temp
        self.head = None
        return self
LL=LinkedList(1,2,3,4,4,5,6)
print(LL)
LL.pop()
print(LL)

LL2 = LinkedList('a', 'b', 'c', 'd', 'e', 'f')
print(LL2)
LL2.pop()
print(LL2)

LL.remove(4)
print(LL, LL.length)

LL2.delete()
print(LL2)