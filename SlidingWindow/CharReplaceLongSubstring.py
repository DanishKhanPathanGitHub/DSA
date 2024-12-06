""""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 
"""
#whenever this type of maximum,, minimum, sub-string/list
#questions come it's sliding window.
#here, we want to find max substring of repeated chars
#replacing k chars allowed, ABAA k=1 means, we cheaat 1 time
#and AAAA, 4
#Bruite force approach would be for each character we go deep into
#untill our window breaks.window of repeatated chars.
#and count  which substring is highest of length

def characterReplacementBruiteForce(s: str, k: int) -> int:
    res = 0
    for i in range(len(s)-1):
        temp_k = k
        #print(f'for {s[i]}: ', end="->")
        for j in range(i+1, len(s)):
            if s[j]==s[i]:
                pass
            else:
                if temp_k:
                    temp_k-=1
                else:
                    break
        #print('len = ', j-i)
        res = max(res, j-i)
    return res
#This code has a bug
# Which is, it's not backward compatible
# ex. ABBB, k=1 Algo will count forward, ignoring backward
# here, for A, res =2, for B it won't look  backward so A will missed
# so for B, res=3, and it should be 4. 
              
print(characterReplacementBruiteForce(s = "AABABBBA", k = 1))

#now we will slid the window linearly
#we move our window linearly from left
#if conditionn break we have to move left 1 step ahead
#that's the basic moto of every sliding window problem
#in the perticular problem how we implement that, is important
#here,we asked for max size of window. what is condition for window
#how long we expand our window
#here, till our window has all repeatative character - k
#so our size of window should not have k number of difrnt elements
#if it gets, we simply do left+=1 and reduce the 
def characterReplacementSlidingWindow(s: str, k: int) -> int:
    count = {}
    l=0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0)+1
        maxf = max(maxf, count[s[r]])
        #frequency of element which occured maximum time in window
        if (r-l+1) - maxf > k:
        #window size - maxf will give how many different characters are in our window
        #it should be no more than k
            count[s[l]] -= 1
            l+=1
    return r-l+1

print(characterReplacementSlidingWindow(s="AABABBBA", k=1))