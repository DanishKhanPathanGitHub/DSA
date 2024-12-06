"""
Visualization:
4,3,1,3,8,2
we compare two elements, and we move higher elements to right
4,3 -> 3,4, now, 4,1 -> 1,4
now 4,3 -> 3,4 now 4,8-> remains 4,8
lastly, 8,2 ->  2,8. 
3,1,3,4,2,8
so in one cycle of comparision we get highest number to most right
now we have to do this comparision of rest of nums, (excluding right as it sorted)

"""

def BubbleSort(nums: list[int]) ->list[int]:
    for i in range(len(nums)-1): #comparision to next element,
        #so excluding right most element 
        for j in range(len(nums)-i-1): #we apply cycle  of comparision on
            #rest of nums, which is how many numbers already sorted
            #which is how many time i loop ran. each time i complete it's loop
            #one element at right get sorted(get it's position)
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] 
    return nums

#O(n^2) O(1) space
print(BubbleSort([4,3,1,3,8,2]))

