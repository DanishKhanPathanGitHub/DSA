'''
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
#Bruite force approach
# first of let us think with using division operator
# for that we can get the total multiplication of array elements
# ex, here for [1,2,3,4] = 24
# then we can divide 24 by each element to get the product of elements except itself
# here catch is for 0, total multiplication would be 0, 
# so for 0 we have to get the multiplication of rest of elements
# ex [-1,1,0,-3,3], total = 0, and for 0 ans should be = 9

def productExceptSelf1(nums): 
        total = 1
        total_0 = 1
        #for 0 element we will count different total
        flag=1
        for num in nums:
            total*=num
            if num == 0 and flag == 1:
                flag=0
                continue
            #we skipped 0 here, so we don't get 0 as total for the 0's total
            #but if there is another 0 in list, total should be 0
            #so we make sure by flage that we skip 0 for 1 time only
            #ex. [-1,1,0,-3,3] for 0, we skip the multiplication & total_0 would be 9
            #but for [0,0,1], even for any of 0's of this list ans would be 0
            #but if we skip 0 for both of them, we will get total_0 as 1
            #that's why we make sure we only skip 0 1 time
            total_0*=num
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = total_0
            else:
                nums[i] = total//nums[i]
        return nums
#that would be O(n+n) O(n) time and O(1)
#but now we should not use the // divide operator as mentioned in the problem

#if we count the postfix and prefix of the number and multiply we will get the ans
#ex. [1,2,3,4] for 1 ans is 24, how we get it?
# prefix of 1 is nothing so 1, and postfix - 2*3*4 = 24
#for 3, postfix is 4, prefix is 2 so 4*2 = 8 is the ans for 3

def productExceptSelf2(nums):
    res = [1]*(len(nums))
    prefix = 1
    #for the first element base prefix set to 1
    for i in range(len(nums)):
        #iterating through all elements
        res[i] = prefix
        #storing the prefix of element as a result in res
        prefix*=nums[i]
        #updating prefix for the next element, it would be prefix*current element
    postfix = 1
    #setting the base postfix for last element of list
    for i in range(len(nums)-1,-1,-1):
        #iterating reversly for counting postfix
        res[i] = postfix*res[i]
        #now multiplying the stored prefix with postfix to get the final answer
        postfix*=nums[i]
        #updating postfix for the next element, it would be postfix*current element
    return res
#O(n+n) time and O(n) space if we count res array as space otherwise it's O(1)

print(productExceptSelf1([1,2,3,4]))
print(productExceptSelf1([-1,1,0,-3,3]))
