class Fibonacci:
    def __init__(self):
        self.memo = {1:1, 2:2}

    def get_fibonaci_element(self, n):
        """returns the nth numbers of fibonacci series"""
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.get_fibonaci_element(n-1) + self.get_fibonaci_element(n-2)
        return self.memo[n]
    
    def get_fibonaci_sum(self, n):
        """returns the sum of fibonacci series including nth element"""
        sum = 0
        for i in range(1,n+1):
            sum+=self.get_fibonaci_element(n)
        return sum

fibonaci = Fibonacci()
print(fibonaci.get_fibonaci_element(10))
print(fibonaci.get_fibonaci_sum(70))


def pattern1(row, col=0):
    if row==0:
        return
    if col >= row:
        print()
        pattern1(row-1, col=0)
    else:
        print('*', end="")
        pattern1(row, col+1)    
pattern1(4)

def bubble_sort(nums, row, col=0):
    if row==0:
        return
    if col >= row:
        bubble_sort(nums, row-1, col=0) 
    else:
        if nums[col] > nums[col+1]:
            nums[col], nums[col+1] = nums[col+1], nums[col]
        bubble_sort(nums, row, col+1)  

nums =[10,5,20,3,7,0]
bubble_sort(nums, 5)

print(nums)


def selection_sort(nums, row, col=0):
    if row==0:
        return
    if col >= row:
        selection_sort(nums, row-1, col=0)
    else:
        if nums[row] < nums[col]:
            nums[row], nums[col] = nums[col], nums[row]
        selection_sort(nums, row, col+1)  

nums =[10,5,20,3,7,0]
selection_sort(nums, 5)

print(nums)
