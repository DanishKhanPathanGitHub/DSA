'''Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.'''

#for that, we will iterate through each element in list except last twp
#and for that element - num we will iterate 2 pointers to rest of the list
#we will get sum of 2 pointers, if sum = -num, it means we found our triplets
#but hold on, for all of that to work we need to sort the list
#bcoz now, if sum < -num, or sum > -num, we have to increase decrease pointers
#for triplets we store them in set, so it will be not contain any duplicates

def threeSum(nums):
        nums = sorted(nums) #O(nlogn)
        ans = set() 
        for i in range(len(nums)-2): #O(n)
            start, end = i+1, len(nums)-1
            while start < end:   #O(n)
                if nums[start]+nums[end] < -nums[i]:
                    start+=1
                    continue
                elif nums[start]+nums[end] > -nums[i]:    
                    end-=1
                    continue
                else:
                    ans.add((nums[start], nums[end], nums[i]))
                    start, end = start+1, end-1
        return list(ans)
#time: o(nlogn + n^2)
#space: O(3n)
print(threeSum([-1,0,1,2,-1,-4]))