def partitionHighIndex(arr, low, high):
    # We are choosing the last element as the pivot
    pivot = arr[high]
    
    i = low - 1  # Index of the smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at index i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1  # Return the partitioning index


def partitionLowIndex(arr, low, high):
    pivot = arr[low]

    i = high+1
    for j in range(high, low, -1):
        if arr[j] >= pivot:
            i-=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i-1], arr[low] = arr[low], arr[i-1]
    return i-1

def partitionMiddle(arr, low, high):
    mid = (low+high)//2
    pivot = arr[mid]

    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[mid] =arr[mid], arr[i+1]
    return i+1        
        
def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partitionHighIndex(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def quick_sort2(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partitionLowIndex(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def quick_sort3(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partitionMiddle(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

arr = [10, 80, 75, 30, 90, 40, 50, 70]  
quick_sort(arr, low=0, high=6)
print(arr)

arr = [10, 80, 75, 30, 90, 40, 50, 70]  
quick_sort2(arr, low=0, high=6)
print(arr)

arr = [10, 80, 75, 30, 90, 40, 50, 70]  
quick_sort3(arr, low=0, high=6)
print(arr)

def quick_sort_copy_arr(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    pivot = arr[mid]

    left = []
    right = []
    for x in arr:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort_copy_arr(left) + mid + quick_sort_copy_arr(right)