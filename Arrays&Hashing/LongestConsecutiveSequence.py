'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9'''

#First lets do it by bruite force aoproach
#we can sort the array, & loop through all nums
# compare 2 consecutive nums to check if they are in sequence 
#if they are in seq, we can update the lcs by +1
# if they are'n, we can append the current lcs to res
# and repeat process still last element
# last we return max of the res
#  other some cases we will look into code
def longestConsecutive1(nums):
    nums = sorted(nums)
    res = [0]
    #for empty array of nums, we can return 0 
    lcs = 1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            lcs = lcs
            #ex, 0,0 will count as it's in sequence but won't update lcs
            #see ex.2
        elif nums[i]==nums[i-1]+1:
            lcs+=1
        else:
            res.append(lcs)
            #if nums are'n in seq, it means seq broke we append current lcs to res
            #and set lcs back to 1 for next numbers of nums
            lcs=1
    if len(nums)!=0:
    #what if last element of num is part of seq
    #ex. [0,1,2], they all in se, so as per above code,
    #we nevere going to get into else case, and won't be appending lcs to res
    # so we append current lcs after loop breaks
    # but if nums is empty, we will not append lcs =1 into res 
        res.append(lcs)

    return max(res)

#This is O(nlogn +n) time, nlogn for sorting and n for loop, and O(n) space
#Now we have to do this O(nlogn) time

#[100, 4, 200, 1, 3, 2] look at this
#every sequence start with number which doesn't have previous num
#that's very obvious lol
#100, if starting point of sequence, 99 should not be in there
# 4 if starting point of sequence, 3 should be not there and likewise
#so we iterate through whole array and find the starting number of sequence 
#if we find sequence num, we simply check till how much it goes,
#we found, 100 is starting point, for 100 we run loop till 100+i doesn't exist in list
#101, is not there, we terminate loop. 
#like wise for 1 we will start loop, 1+1=2 exist, 2+1=3exist, 3+1=4 exist, 4+1=5 not
#we terminate loop
def longestConsecutive2(nums):
    nums_set = set(nums)
    lcs = 1
    for num in nums:
        if num-1 in nums_set:
            #means it's not a starting point of sequence
            continue
        else:
            #if it's starting point of sequence
            num_lcs = 1
            #we count lcs for that number
            while True:
                if num+1 in nums_set:
                    #see how long sequence goes
                    num_lcs+=1
                    num = num+1
                else:
                    break
            if num_lcs > lcs:
                #we see if lcs for this number is > lcs if so we update it
                lcs=num_lcs
    return lcs

print('test case1 result', longestConsecutive1([0,0]), 'ans should be 1')
print('test case1 result', longestConsecutive1([0]), 'ans should be 1')
print('test case1 result', longestConsecutive1([0,100,3,1,2]), 'ans should be 4')

print('test case1 result', longestConsecutive2([0,0]), 'ans should be 1')
print('test case1 result', longestConsecutive2([0]), 'ans should be 1')
print('test case1 result', longestConsecutive2([0,100,3,1,2]), 'ans should be 4')