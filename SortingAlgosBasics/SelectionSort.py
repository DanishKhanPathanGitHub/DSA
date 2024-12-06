"""
In bubble sort we compared two elements and swap
in sleection we compare each element with first element 
and swap if it's less
so in each cycle we will get the first/left side of element as sorted/less
4,3,1,5,2
4,3 swap-> 3,4, now 3,1 swap, 1,3(actually, 1,4,3), 1,5 no swwap, 1,2 no swap
that's how we get minimum number at left side
we do that for each element
"""
def SelectionSort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums

#O(n^2) time O(1) space
print(SelectionSort([4,3,1,5,2]))
