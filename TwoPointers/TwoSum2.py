#slidding windiw:
#we take 2 pointers 1 starting element and 1 ending element
#and we move thiss pointers accordingly to right and left
# see the problem of below
# we have list already sorted and same problemm as two sum before
#[1,3,4,5,7,10,11] target = 9
# we take 2 pointers start=1, and end=11, 1+11=12 which is > target
# what does it mean? it means that we have to take number lesser
# how do we get that? moving end point left, bcoz nums are sorted in ascending order 
# 1,10 1+10=11 still>9, 1,7=8<9 so moving start point right.
#3,7=10>9, 3,5=8<9, 4,5=9 yeaaaaaaaah babyyyyyyyyy
def TwoSumPointers(nums, target):
    left, right = 0, len(nums)-1
    while True:
        sum = nums[left]+nums[right]
        if sum > target:
            right-=1
        elif sum < target:
            left+=1
        else:
            return [left, right]
        
print(TwoSumPointers([1,3,4,5,7,10,11], 9))