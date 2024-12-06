'''
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''
# One obvious solution would be counting the frequency of each element in nums
# and storing num:frequency as key:value in a dict
# then sorting that dict by values in descending order
#returning the first k keys
def TopK1(nums, k):
    count = {}
    for num in nums:#O(n)
        count[num] = 1+count.get(num, 0)
    res = list(dict(sorted(count.items(), key=lambda item:item[1], reverse=True)).keys())
    #O(nlogn)
    return res[:k]

print(TopK1([1,1,1,2,2,2,3], k = 2))
#this will take O(nlogn + n)
#now we will again count the frequency same way as above in count dictionary
# Now, for a list of length n, any element can be occured maximum as n times
# we will use index of to represent the nums occured index amount of time
# like, [1,1,1,2,2,2,3] n=7, we will make list of n+1 = 8. 
# bcoz max time a num can occur=7, 7th index represents the nums occured 7 times
# likewise 0 index represent nothing 
# & 1 to 7 index represents the nums occuring that times
# so we need 8 as n+1 length of list
#we will traverse that reversly as to find top frequency nums
def TopK2(nums, k):     
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    for num in nums:
        count[num]=count.get(num, 0)+1
    for n, c in count.items():
        freq[c].append(n)
        #here, 1 occurs 3 time, so we will append 1 to freq[3]
        # same for 2, so we will append 2 to freq[3] also
        # and 3 occurs 1 time so, frq[1] will have [3] 
    res = [] 
    #after this we will have freq something like this below:
    #[[], [3], [], [1,2], [], [], [], []]
    for i in range(len(freq)-1, 0, -1):
        #traversing list in reverse
        for num in freq[i]:
            res.append(num)
            if len(res)==k:
                return res
        #n + n + kn = n(2+k) time and n+n+k=2n+k space  
print(TopK2([1,1,1,2,2,3,3,3,3,3,4], k = 4))