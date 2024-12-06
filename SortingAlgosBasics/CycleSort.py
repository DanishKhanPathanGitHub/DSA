
#frist we will do for the list which have 1 to n numbers

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i]   
        # Find the index where the current element should be
        if nums[i] != nums[correct_index]:
            # Swap the current element with the element at its correct position
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    return nums

# Example usage
List = [3, 1, 5, 0, 4, 2]
sorted_list = cyclic_sort(List)
print(sorted_list)  # Output: [1, 2, 3, 4, 5]

#Missing number 0, n
def missingNumber(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i]   
        # Find the index where the current element should be
        if nums[i] < len(nums) and nums[i] != nums[correct_index]:
            # Swap the current element with the element at its correct position
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    return nums