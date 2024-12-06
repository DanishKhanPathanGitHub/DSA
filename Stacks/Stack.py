myStack = []
myStack.append('a') 
myStack.append('b')
myStack.append('c')
print(myStack)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
try:
    print(myStack.pop())
except:
    print(myStack)
#list can be used as stack as they has push method as append
#and pop method as well. but disadvantage is append method
#bcz python list elements has continuous memory allocation
#when list is initialized it initialized with some memory, when 
#list run out of that memory and append method call'
#it need etc memory allocation operation as well
#so using linked list solve this problem as we can just add the 
#next element which doesn't have to worry about memory allocation
#as it's random
print("<---custom stack using deque----->")
from collections import deque

class Stack:
    def __init__(self):
        self._elements = deque()

    def pop(self):
        return self._elements.pop()

    def append(self, element):
        self._elements.append(element)

    def __repr__(self):
        values = []
        for val in self._elements:
            values.append(val)
        return "|".join(values)

myStack = Stack()
myStack.append('a')
myStack.append('b')
myStack.append('c')
print(myStack)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
try:
    print(myStack.pop())
except:
    print(myStack)

#ohkay but let's do some real problem to undestand
"""
Validate Parentheses
You are given a string s consisting of the following characters: 
'(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.
"""
#This is not intuative if we do not understand stack 
#when any closing bracket comes, his previous bracket if it's opening,
#should be the same type
#what i mean is look at example 3. 
#where if u think at the end, [ is closed by ] in s. but it's not like that
#( is closed by ]
#so what we going to do is first we have to map the opening brackets to their closing brackets
#then, when any opening bracket comes we append in stack/list
#if any closing bracket come we do not append it into stack
# we pop the stack which is last appended opening bracket
#so we will compare poped bracket and the closing bracket are they of same type
#if so we will continue otherwise we will return False'
#if there is confusion, keep in mind we will not have any closing brackets 
#in our stack, we will have only opening bracket, whenever any closing bracket comes
#we just compare it with last added bracket in stack which is opening bracket

def isValid(s: str) -> bool:
    map = {')':'(', '}':'{', ']':'['}
    stack = []
    for c in s:
        if c in map and stack:
            #that mean it's closing bracket
            open = stack.pop()
            #we appended last bracket which is opening, from stack
            if map[c] != open:
                #we get opening bracket coresponding to closing bracket from map
                #if not same then we return True otherwise nothing
                return False
        else:
            #that means it opening bracket
            stack.append(c)
    
    #now if all bracket closed stack should be empty
    return not stack

print(isValid("[({[]})]"))
print(isValid('{[}]'))