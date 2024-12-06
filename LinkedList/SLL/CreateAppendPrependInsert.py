class Node:
    """
    creates a node with
    .value set to value provided in arg
    .next set to None
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    """
    accepts *args: any number of args as values
    creates a Linked List containing all1 values
    """
    def __init__(self, *values):
        """
        each value from *values - args get appended inton Linked List
        """
        self.head = None
        self.tail = None
        self.length = 0
        for value in values:
            self.append(value)
            
    
    def append(self, value):
        """
        creates a node with value from arg
        checks if head & tail is set or not, if not then set node as head & tail
        otherwise, set current tail elements .next to our new node
        and finall1y set our new node as .tail  
        """
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length+=1
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.length+=1
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        if not self.tail:
            self.tail = new_node
        
        self.length += 1

    def insert(self, value, index):
        """
        inserts the node with given value at given index
        
        Parameters:
        -----------
        value:
            int: mandatory
        index:
            int: mandatory
            0 <= index <= self.length
        returns:
            None
        """
        if index < 0 or index > self.length:
            raise IndexError("index out of range")

        if index == 0:
            self.prepend(value)
            return

        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)
        curr_node = self.head
        for i in range(index - 1):
            curr_node = curr_node.next
        
        new_node.next = curr_node.next
        curr_node.next = new_node
        self.length+=1
        return

    def __repr__(self):
        nodes = ''
        current_node = self.head
        while current_node:
            nodes= nodes+str(current_node)+' -> '
            current_node = current_node.next
        return nodes+'None'

# Example usage

LL1 = LinkedList()
LL1.prepend(10)
print(LL1, LL1.length)
LL1.append(12)
LL1.append(13)
LL1.append(14)
LL1.append(15)
#append method is O(1) time and space
#creating n nodes LL1, takess O(n) time and space
print(LL1, LL1.length)

LL2 = LinkedList(1,2,3,4,5)
print(LL2)
LL2.insert(4, 2)
print(LL2)