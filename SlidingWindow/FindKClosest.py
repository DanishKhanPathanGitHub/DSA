"""
658. Find K Closest Elements
Given a sorted integer array arr, two integers k and x, 
return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""
#bruite force way to solve this is recording difference between 
# each element and target-x, we will store difference as key
#and number as value
#then we will sort the dictionory basen on key - which is difference''
#then we will fetch the values which are num and will give output

def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
        from collections import defaultdict
        l, r = 0, k-1
        res = defaultdict(list)
        for num in arr:
            dif = abs(x-num)
            res[dif].append(num)
            #for the same dofference there can be multiple values
        res_sorted = sorted(res)
        print(res_sorted)
        output = []
        for key in res_sorted:
            for num in res[key]:
                output.append(num)
        return sorted(output[:k])
#O(nlogn) #as sorting involved

#now we have to make it sliding window way
#we were given the window size which is k, 
#we need to find the index of x in array, or if won't find we find the closest
#then we will set it to r, and index of x - k +1 as l
#this is our window, not what we wil do is we will check
#left-x > right-x, if so we will move left and right one ahead
# untill we found right window
# but age cases like, [1,2,3,4,5], x=3, k=4
# now x=3 is at 2th index and 2-4+1 = -1, which can't be left
# so in that case, l=0, r = 2th index + abs(2-4+1)  
def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:   
    #finding index
    l, r = 0, len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if x >  arr[mid]:
            l+=1
        elif x < arr[mid]:
            r-=1
        else:
             break
    r=mid-1
    l=0
    if r-k+1 < 0:
        l=0
        r=r+abs(r-k+1)
    else:
        r=r
        l=r-k+1
    while True:
        if r==len(arr)-1:
            break
        else:
            if abs(x-arr[r+1]) < abs(x-arr[l]):
                l, r = l+1, r+1
            else:
                break
    print(arr[l:r+1])

findClosestElements([1,2,3,4,5], k=3, x=3)