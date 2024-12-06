class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    

class CircularSinglyLinkedList:
    """
    Constructor:
    takes *values and creates Node(value) objects for each
    Last Node(value).next = self.head

    methods:
    -------
    append(value):
        appends the node with given value
    length():
        returns the length of LinkedList object
    insert(value, index):
        insert the node with given value at give index(starts with 0)
    pop():
        Remove last node from the linked list
    remove(index):
        Remove the node at given index(starts with 0)
    """
    def __init__(self, *values):
        self.head = None
        for value in values:
            self.append(value)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = node
            node.next = self.head

    def __repr__(self):
        nodes = []
        current_node = self.head
        if current_node is None:
            return 'None'
        while current_node.next != self.head:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        nodes.append(str(current_node.value))
        return ' -> '.join(nodes) + ' -> HEAD'

    def length(self):
        if not self.head:
            return 0
        count = 1
        curr = self.head
        while curr.next != self.head:
            count+=1
            curr=curr.next
        return count

    
    def insert(self, value, index):
        """
        insert the node with given value at give index
        Params:
        -------
        value:
            int, 
        index:
            int, 0 <= index <= self.length
            otherwise raises index error
        return:
            None
        """
        if index < 0 or self.length() < index:
            raise IndexError("Index out of bounds")
        
        node = Node(value)
        if index == 0:
            if not self.head:
                self.head = node
                node.next = self.head
            else:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                self.head = node
                node.next = curr.next
                curr.next = node
            return
        
        curr = self.head
        for i in range(index - 1):
            curr = curr.next
        
        node.next = curr.next
        curr.next = node
        return
    
    def pop(self):
        """
        Remove last node from the linked list

        return:
        -------
        pop_value:
            value of the node which popped
        Raises:
            index error on call on empty list
        """
        if not self.head:
            raise IndexError("Pop from an empty list")
        curr = self.head
        while curr.next.next != self.head:
            curr = curr.next
        if curr == self.head:
            pop_value = self.head.value
            self.head = None
            return pop_value
        

        pop_value = curr.next.value
        curr.next = self.head
        return pop_value
    
    def remove(self, index:int):
        """
        removes the node at given index
        paramas:
        -------
        index:
            int
            0<=index<=self.length
            raises indexError
        return:
            None
        """
        if index > self.length() or index < 0:
            raise IndexError("Index out of bounds")

        curr = self.head
        if index == 0:
            if self.head.next == self.head:  # Only one node
                self.head = None
                return
            while curr.next != self.head:
                curr=curr.next
            curr.next = self.head.next
            self.head = self.head.next
            return 
        1
        for i in range(index - 1):
            curr = curr.next

        #node to get removed: curr.next
        curr.next = curr.next.next
        return


CSLL = CircularSinglyLinkedList(1,2,3,4,5)
print(CSLL, " after creation", CSLL.length())
CSLL.append(2)
print(CSLL, " after appending 2", CSLL.length())
CSLL.insert(4, 6)
print(CSLL, " after inserting 4 at index 6", CSLL.length())
CSLL.insert(3, 6)
print(CSLL, " after inserting 3 at index 6", CSLL.length())
CSLL.insert(0, 0)
print(CSLL, " after inserting 0 at index 0", CSLL.length())
CSLL.pop()
print(CSLL, " after poping", CSLL.length())
CSLL.remove(6)
print(CSLL, " after removing node at 6th index", CSLL.length())
CSLL.remove(6)
print(CSLL, " after removing node at 6th index/which is last", CSLL.length())
CSLL.remove(0)
print(CSLL, " after removing node at 0th index", CSLL.length())
CSLL = CircularSinglyLinkedList(1)
print("-------<new CSLL created>-----", CSLL)
CSLL.pop()
print(CSLL, " after poping", CSLL.length())
CSLL.append(1)
print(CSLL, " after appending to empty list", CSLL.length())
CSLL.remove(0)
print(CSLL, " after removing from list which contains only one node", CSLL.length())
