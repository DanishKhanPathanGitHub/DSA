"""
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, 
return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
#again this problem where we given window - t, 
#so problem is like, we will slide our window on main - 2
#and we will see if the given window exist in our window
#so counting will be there
#bruite force approach would be, starting from each element,
#we will go deep until we found given window -t in our window -s
#That you can do but we won't
#what better we can do to do it in linear is the question
#As we can understand we just don't need to count new window each time
#we will start with sliding window, untill first we match the given window
#when we match the window, we will now remove left elements from window'
#untill our window won't match the givem window, 
#through this process we will keep updating result
#when condition broken down, we then move window rigghtwards untill matches
#this process will repeated till we broke our last window & we reach right most

def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return False
    s_count = {} #our window
    t_count = {} #given window
    for c in t:
        t_count[c] = 1+t_count.get(c, 0)
    have, need = 0, len(t_count) 
    #we will keep track of how given window count nd our window count 
    #we will match them, and update results if satisfied
    res, resLen = [-1, -1], float("infinity")
    #initial results for matching, we will se why they set like that
    l=0
    for r in range(len(s)):
        s_count[s[r]] = 1+s_count.get(s[r], 0)
        if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
            have+=1
        #means that we have one character in our window of same count as in given window

        #now if have matches need, means we have all characters of given window in our window
        #now we will update result and left pointer untill we break our window
        while have == need:
            if r-l+1 < resLen:
                #now we have to find shortest, so that's why 
                #initial comparision should be most high so initial condition get passed
                res = [l, r]
                resLen = r-l+1 #that's length of our current window

            s_count[s[l]]-=1
            #decrease counter of left pointer
            if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                #now if decreasing left counter doesn't mean our windows break
                #it does not break in 2 conditions,
                #1 is when left character we decreased wasn't in given window
                #so it won't affect the updated window
                #2nd is when decreeased character still have same or 
                #more amount of characters in updated window
                #ex. BBABC, if we have to find AB,
                #we are at BBA, where our have==need condition first time matched
                #now removing left B, BA is updated window
                #but it won't affect have, beacuse we still have, B's counter same as we need
                #it will only break condition of have when it will be less than what we need 
                #means in t_count - given window
                have-=1
                #so that both condition satisfies, we decrease have by 1
            l+=1         
    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ""
    
print(minWindow("ADOBECODEBANC", t = "ABC"))