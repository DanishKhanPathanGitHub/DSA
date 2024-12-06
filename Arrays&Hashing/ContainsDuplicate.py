'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
'''
'''
sol1: make a hashmap, store the num:1 key:value, 
check if num exist in that hashmap, if, then return True, else add that num
Array operation for searching and appending is time consuming more than hashmap
'''
import time
def containsDuplicateUsingHashmap(nums):
        if len(nums) < 2:
            return False
        nums_duplicate = dict()
        for num in nums:
            if num in nums_duplicate:
                return True
            else:
                nums_duplicate[num] = 1
        return False

#O(N) Time complexity and O(N)
#bruite force(comparing each num to each) would be O(N^2) time, but O(1) space
#O(NlogN) time and O(1) space for sorted array
'''
for sorted array we just need to compare neighbour elements
rather than iterating whole array for every element like in bruit force
'''
def containsDuplicateUsingSortedArray(nums):
    if len(nums) < 2:
        return False
    sorted_nums = sorted(nums)
    for i in range(0, len(sorted_nums)-1):
        if sorted_nums[i]==sorted_nums[i+1]:
            return True
    return False

import random

nums = list(range(1, 2000000))
random.shuffle(nums)
nums = nums[:50000]

t1=time.perf_counter()
print(containsDuplicateUsingHashmap(nums))
t2=time.perf_counter()
print(format(t2-t1, '0.6f'))

t3=time.perf_counter()
print(containsDuplicateUsingSortedArray(nums))
t4=time.perf_counter()
print(format(t4-t3, '0.6f'))
