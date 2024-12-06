def in_place_merge(List, start, mid, end):
    # Define two pointers for the two sublists
    L1 = start
    L2 = mid + 1

    while L1 <= mid and L2 <= end:
        if List[L1] <= List[L2]:
            L1 += 1
            print(L1)
        else:
            # List[L2] is smaller, we need to place it in the correct position
            value = List[L2]
            index = L2

            # Shift all elements from L1 to L2-1 to the right by one position
            while index > L1:
                List[index] = List[index - 1]
                index -= 1
            
            # Place the smaller element in the correct position
            List[L1] = value

            # Update pointers
            L1 += 1
            mid += 1
            L2 += 1
            print(L1, mid, L2)

def in_place_merge_sort(List, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2

    # Sort the first half
    in_place_merge_sort(List, start, mid)

    # Sort the second half
    in_place_merge_sort(List, mid + 1, end)

    # Merge the two sorted halves
    in_place_merge(List, start, mid, end)

# Example usage
List = [38, 27, 43, 3, 9, 82, 10, 34]
in_place_merge_sort(List, 0, len(List) - 1)
print(List)
