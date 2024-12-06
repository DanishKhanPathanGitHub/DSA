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

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.length += 1

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
    
    def get(self, index):
        """
        returns the Node at given index
        
        Parameteres:
        index:
            int: 
            index < self.length, raises index error otherwise
            0 or +ve sign will get the node from head
            -ve sign will get the index'th node from tail
        return:
            <Node obj>
        """
        if index < -self.length or index >= self.length:
            raise IndexError('Index out of range')

        # Adjust negative indices
        if index < 0:
            index = self.length + index

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        
        return current_node
        

    def find(self, value, start=0, n=1):
        """
        Returns the index of the nth occurrence of the node with the given value,
        starting the search from the given start index. Returns -1 if not found.

        Parameters
        ----------
        value : any
            The value to be searched in the list.
        start : int, optional
            The index from which to start the search (default is 0).
        n : int, optional
            The occurrence number to find (default is 1).

        Returns
        -------
        int
            The index of the nth occurrence of the node with the given value,
            or -1 if not found
        """
        if start < 0 or start >= self.length or n <= 0:
            return -1

        current = self.head
        index = 0
        occurrences = 0

        # Move to the start index
        while index < start and current:
            current = current.next
            index += 1

        # Search for the value
        while current:
            if current.value == value:
                occurrences += 1
                if occurrences == n:
                    return index - start
            current = current.next
            index += 1

        return -1
    
    def update(self, index, value):
        """
        update the value of node at given index with given value
        Parameters:
        -----------
        index:
            int: < self.length && > 0
            Raises IndexError
        If the index is out of range.
        value:
            any
        return:
            None
        """

        if index < 0 or index >= self.length:
            raise IndexError('Index out of range')

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.value = value

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(nodes) + ' -> None'


if __name__ == "__main__":
    LL = LinkedList(9, 10, 12, 13, 10)
    print("Original List:")
    print(LL)

    LL.append(15)
    print("\nAfter appending 15:")
    print(LL)
    
    print("\ngetting the elements at index")
    print(LL.get(2))
    print(LL.get(-2))

    print("\nfinding indexes with diffreent params:")
    print(LL.find(15, start=2))
    print(LL.find(10, n=2))

    LL.update(0, 10)
    LL.update(1, 11)
    LL.update(4, 14)
    print("\nLL after update")
    print(LL)