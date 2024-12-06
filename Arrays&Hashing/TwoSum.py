'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
#iterating through array and find if target-element exist or not
#if exisst then we return the index of element and target-element
def twoSumUsingIteration(nums, target):
    for i in range(len(nums)-1):
        if target-nums[i] in nums[i+1:]:
            return [i, nums.index(target-nums[i], i+1)]
    return [0,0]
#O(n) time and O(1) space


import time
nums = list(range(1, 20000))

t1 = time.perf_counter()
print(twoSumUsingIteration(nums, 39997))
t2 = time.perf_counter()
print(format(t2-t1, '0.8f'))


