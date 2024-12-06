""""
palindrom means same word in reverse
ex. 'SaaS', 'aabaa'
#easily we take reverse of string and compare it
#for problem ignoring case sensitivity and non-alphanumeric characters,
#reverse won't work. we can create a new string containing only alphanumeric chars
#which requires extra memory.
#see that's good solution but we want to solve it by 2 pointers
2 pointers are perfect for this problem 
we will check 2 pointers are same and move each pointer left and right
"""
def ValidPalindrom(str):
    left, right = 0, len(str)-1
    def isAlphaNumeric(char):
        return (ord('A')<=ord(char)<=ord('Z') or
                ord('a')<=ord(char)<=ord('z') or
                ord('0')<=ord(char)<=ord('9'))
    while left < right: #that's where we stop comparing.
        if isAlphaNumeric(str[left])==False:
            left+=1
            continue
        if isAlphaNumeric(str[right])==False:
            right-=1
            continue
        if str[left].lower()==str[right].lower():
            left+=1
            right-=1
        else:
            return False
    return True

print(ValidPalindrom('SAaS'))
print(ValidPalindrom('a!--!"aBA-a'))
print(ValidPalindrom('SSa'))