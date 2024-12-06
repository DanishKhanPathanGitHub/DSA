'''
visualization and explaination:
4,1,3,9,0
we keep first element as smallest, start our loop from 1 index
here, 4, starting from 1
now, we compare 1 to all elements before it
if element is > 1, we move that element 1 right,
when we broke condition of elements > 1 before it, 
we stop and insert 1 at that position
we compare 1 to 4, so we move 4 one right, now there is no elements before it
loop will break, 1 will be inserted to left side, 1,4
now 3, it will make case clear
3 < 4, 3<1 no, so break and insert 3 next to 1
1,3,4 now for 9, 9<4 no, so insert 9 next to 4, now 1,3,4,9
now 0, 0<9, 0<4, 0<3, 0<1, so insert 0 at most left
'''

#4,1,3,9,0
def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i] #element to compare
        j = i - 1 #index of right most element of elements before key
        #we have to compare key with elements before key
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            #moving nums[j] to one right
            #for key=1, j=0, nums[0] = 4, 1<4, so
            #[4,1,3,9,0] here, 1 will become 4, as 4 moveed 1 right 
            j -= 1
            #j = 0-1 = -1
            #[4,4,3,9,0], 1 will be inserted to -1+1=0th position
            #see below code
        nums[j + 1] = key
        #nums[-1+1] = 1 [1,4,3,9,0]
        #when key is not < element we compare, we move key right
        #for all elements < key, here j would be -1, so -1+1 =0
        #at 0th position it will be inserted
    print(nums)
    return nums

insertionSort([4,1,3,9,0])

#Linked List insertion sort
class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self, val): 
        node = Node(val)
        node.next = None
