'''
11. Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by 
array [1,8,6,2,5,4,8,3,7]. In this case, 
the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
'''
#for better visualization see the leetcode
#basically here, index of height list reprs x axes, and value-height reprs y axes
#ex. here 2nd element 8 has (1, 8) point, means 8 is height
#now to calculate how much water a container contain we can find it's area
#for that we have to find distance between two lines, and minimum height from 2 lines
#becoz, for lines b|w height of 8 and 2, water will be contain till height 2
#not till 8, so for the counting area we take min height
def maxArea(height):
    max_area = 0
    for i in range(len(height)-1): #O(n)
        for j in range(i+1, len(height)): #O(n)
            d = j-i #i and j indexes reprs the x axes points
            h = min(height[i], height[j])
            area = d*h
            if area > max_area:
                max_area = area
    return max_area 
#time: O(n^2) space: O(1)
print(maxArea([1,8,6,2,5,4,8,3,7]))
#O(n) solution:
def maxArea2(height):
    max_area = 0
    left, right = 0, len(height)-1
    while left < right:
        area = (right-left)*min(height[right], height[left])
        if area > max_area:
            max_area = area
        if height[right] > height[left]:
            left+=1
        else:
            right-=1        
        
    return max_area

print(maxArea2([8,8,8,8,8,8,8]))

