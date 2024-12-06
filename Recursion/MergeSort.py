import time

def merge(List1:list, List2:list) -> list:
    op = []
    L1, L2 = 0, 0
    while L1 < len(List1) and L2 < len(List2):
        if List1[L1] < List2[L2]:
            op.append(List1[L1])
            L1+=1
        else:
            op.append(List2[L2])
            L2+=1
    if L1 < len(List1):
        op.extend(List1[L1:])
    if L2 < len(List2):
        op.extend(List2[L2:])
    return op

def MergeSortRecursion(List:list):
    mid = len(List)//2
    if mid==0:
        return List
    
    List = merge(MergeSortRecursion(List[0:mid]), MergeSortRecursion(List[mid:]))
    return List


def merge_with_index(List, start, mid, end):
    L1 = start
    L2 = mid+1

    while L1<=mid and L2<=end:
        if List[L1] < List[L2]:
            L1+=1
        else:
            value = List[L2]
            idx = L2

            while idx > L1:
                List[idx] = List[idx-1]
                idx-=1

            List[idx] = value
            L1+=1
            mid+=1
            L2+=1

def merge_sort_in_place(List:list, start, end):
    if start >= end:
        return
    
    mid = (start + end)//2
    merge_sort_in_place(List, start, mid)
    merge_sort_in_place(List, mid+1, end)

    merge_with_index(List, start, mid, end)


nums = [2,1,3,-10,9,-4]
merge_sort_in_place(nums, 0, len(nums)-1)
print(nums)

