"""
567. Permutation in Stringt
Given two strings s1 and s2, return true if 
s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

#what's bruiteforce way, 
#see, in this problem we don't have to find the window
#we had given the window - substring, we have to confirm window exit orr not
#and in this type of problem we have to count the window elements - that's a trick
#so we will count window first, and slid it onto the main string
#like ex, here, ab is of 2 length, we will keep sliding two length on s2
#ei, then, id, then db, then ba. each time we will compare our window counter
#to window we sliding on s2

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2)<len(s1):
        return False
    from collections import Counter
    s1_count = Counter(s1)
    l, r = 0, len(s1)-1
    while r < len(s2):
        s2_count = Counter(s2[l:r+1]) 
        if s2_count == s1_count:
            return True
        else:
            l, r = l+1, r+1
    return False
#O(n.m) n=len of s2, m = lens1
print(checkInclusion("ab", "eaidbooo"))

#can we do this in linear time
#each time we count the window size on s2, when we only update one character at time
#so we have to keep trackk of count of window, rather than counting each time
#that's a trick all other explaination in code

def checkInclusionLinear(s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        length = len(s1)
        l=0
        from collections import Counter
        s1_count = Counter(s1)
        s2_count = {}
        for i in range(len(s1)):
            s2_count[s2[i]] = s2_count.get(s2[i], 0)+1
        #just counted initial window on s2
        r = length-1
        while r < len(s2):
            if s2_count == s1_count:
                return True
            else:
                #we have to add the next element to our window
                #and remove left element
                #but for that we need to check we had reached at end
                if r+1==len(s2):
                    return False
                if s2[l] in s2[l+1:r+1]:
                #now we had some condition for just delete left element
                #or decrease it's count based on element present in next window
                    s2_count[s2[l]]=s2_count.get(s2[l], 0)-1
                else:
                    del s2_count[s2[l]]
                #adding next element(actually increasing count)
                s2_count[s2[r+1]]=s2_count.get(s2[r+1], 0)+1
                l, r = l+1, r+1
        return False

print(checkInclusionLinear("ab", "eaidbooo"))