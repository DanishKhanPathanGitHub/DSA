class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self, *values):
        self.head = None
        self.tail = None
        self.length = 0
        for value in values:
            self.append(value)
    
    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.value))
            curr = curr.next
        return "<->".join(nodes)

    def append(self, value):
        """
        appends the node with value at the end of List
        params:
        -------
        value:
            creates a node with given value
            appends it to List on which method called on
        return:
            None
        """
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length+=1
        return
    
    def insert(self, value, index):
        """
        Insert the node with given value at given index
        params:
        -------
        value:
            creates a node wthi given value
        index:
            insert the node at given index
        raises:
            IndexError if index is not in bound
            0 <= index <= self.length
        """
        if self.length < index or index < 0:
            raise IndexError("index out of bound")
        
        node = Node(value)
        if index==0:
            if not self.head:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.length+=1
            return
        
        if index == self.length:  # If inserting at the end
            self.append(value)
            return
        
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        
        node.next = curr.next
        curr.next.prev = node
        curr.next = node
        node.prev = curr
        
        self.length += 1
    
    def get(self, index):
        """
        return the node at given index
        params:
        -------
        index:
            int
        raises:
            IndexError if index out of bound
            index >= self.length 
        return:
            node at given index
            negative index counts starts from last node to reverse in order
        """
        if abs(index) >= self.length:
            raise IndexError("index out of bound")
        
        # Adjust negative indices
        if index < 0:
            index = self.length + index

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr
    
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
                    return index
            current = current.next
            index += 1

        return -1
    
    def pop(self):
        """
        remove the last node and returns it
        raises:
        -------
        buuffer error if List is empty 
        """
        if not self.tail:
            raise IndexError("List is empty")
        removed_node = self.tail
        if self.tail == self.head:  # Only one element
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return removed_node
    
    def remove(self, index=None, value=None):
        """
        Removes the node at the given index or node with given value
        if both given raises error. 
        removes the first occurence of node with given value

        params:
        index
            int or None by default
            negative index starts from last node to reverse count
        value
            any or None by default
        
        raises:
        --------
        IndexError 
            if index out of bound
            index >= self.length 
        ValueError
            if None of parameter given or both parameter given
        
        return
            Removed Node
        """
        if (index is not None and value is not None) or (index is None and value is None):
            raise ValueError(
                "Provide either 'index' or 'value', not both or none."
            )

        if index is not None:
            if abs(index) >= self.length:
                raise IndexError("index out of range")

            if index < 0:
                index = self.length + index

            if index == self.length - 1:
                return self.pop()

            curr = self.head
            for _ in range(index):
                curr = curr.next

        else:
            curr = self.head
            while curr and curr.value != value:
                curr = curr.next
            
            if not curr:  # Value not found
                raise ValueError(f"Value {value} not found in the list.")

        removed_node = curr
        if removed_node == self.head:
            self.head = curr.next
            if self.head:  # When removing the only element, self.head could be None
                self.head.prev = None
        elif removed_node == self.tail:
            self.tail = curr.prev
            self.tail.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.length -= 1
        return removed_node

DLL = DoublyLinkedList(2)
print(DLL)
DLL.insert(4,1)
print(DLL)
DLL.insert(1,0)
print(DLL)
DLL.insert(3,2)
print(DLL)
DLL.append(5)
print(DLL)
print(DLL.get(0), DLL.get(2), DLL.get(4))
DLL.insert(2, 3)
DLL.append(2)
DLL.append(4)
print(DLL)
print(DLL.find(4,5), DLL.find(2,2,2))
print(DLL.pop(), DLL.pop())
print(DLL)

print("-----<remove by index test>-----")
dll = DoublyLinkedList(10, 20, 30, 40, 50, 60)
print(dll)  # Expected: 10<->20<->30<->40<->50<->60
# Remove from the beginning (index 0)
removed_node = dll.remove(index=0)
print(removed_node)  # Expected: 10
print(dll)           # Expected: 20<->30<->40<->50<->60
# Remove from the end (last index)
removed_node = dll.remove(index=dll.length-1)
print(removed_node)  # Expected: 60
print(dll)           # Expected: 20<->30<->40<->50
# Remove from the middle (index 2)
removed_node = dll.remove(index=2)
print(removed_node)  # Expected: 40
print(dll)           # Expected: 20<->30<->50
# Remove using a negative index (index -1)
removed_node = dll.remove(index=-1)
print(removed_node)  # Expected: 50
print(dll)           # Expected: 20<->30
print("-------<Remove by Value>-------")
# Remove a value from the beginning
removed_node = dll.remove(value=20)
print(removed_node)  # Expected: 20
print(dll)           # Expected: 30
# Add new values and remove a value from the middle
dll.append(40)
dll.append(50)
dll.append(60)
print(dll)           # Expected: 30<->40<->50<->60
removed_node = dll.remove(value=50)
print(removed_node)  # Expected: 50
print(dll)           # Expected: 30<->40<->60
# Remove the tail by value
removed_node = dll.remove(value=60)
print(removed_node)  # Expected: 60
print(dll)           # Expected: 30<->40
print("---------<3. Error Cases:>--------")
# Try to remove a value not in the list
try:
    dll.remove(value=100)
except ValueError as e:
    print(e)  # Expected: "Provide either 'index' or 'value', not both or none."
# Try to remove using an out-of-bound index
try:
    dll.remove(index=5)
except IndexError as e:
    print(e)  # Expected: "index out of range"
# Try to remove without providing either index or value
try:
    dll.remove()
except ValueError as e:
    print(e)  # Expected: "Provide either 'index' or 'value', not both or none."
# Try to remove by providing both index and value
try:
    dll.remove(index=1, value=40)
except ValueError as e:
    print(e)  # Expected: "Provide either 'index' or 'value', not both or none."
# Remove all remaining elements
removed_node = dll.remove(index=0)
print(removed_node)  # Expected: 30
print(dll)           # Expected: 40

removed_node = dll.remove(index=0)
print(removed_node)  # Expected: 40
print(dll)           # Expected: (empty list)
# Try to remove from an empty list
try:
    dll.remove(index=0)
except IndexError as e:
    print(e)  # Expected: "index out of range"
