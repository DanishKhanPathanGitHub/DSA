"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
#bruite force approach would be finding all substring which do not have repitative chars 
#and finding longest of them
#starting from first char, go deep untill we break the condition:
#find repeatative char, doing for all chars
#this will make nlogn

def lengthOfLongestSubstringBruitForce(s: str) -> int:
    res = 0
    for i in range(len(s)-1):
        c_set = {s[i]}
        print("for ", c_set, end=":")
        for k in range(i+1, len(s)):
            if s[k] in c_set:
                break
            else:
                c_set.add(s[i+1])
        print(c_set)
        if len(c_set) > res:
            res = len(c_set)
    return res

print(lengthOfLongestSubstringBruitForce("bbaaabcb")) 

#now what we can do better here is
#applying window
#we can srom left char start go deep untill we break our window
#which is finding the same repeatative char
#then we need to update the window, 
#we move our left to the next character, which get repeatated
#just like above we made seprate set for stroing substring for each vchar
#we will not do that, instead we will make that set as our window
#we will update our window just as i mentioned above

def lengthOfLongestSubstringSlidingWindow(s: str) -> int:
    substring = set()
    left = 0
    res = 0
    for r in range(len(s)):
        while s[r] in substring:
            #before we add tge character into our window,
            #we want to check if that character present in our window
            #it can be present at any position
            #so we keep removing left elements from the window
            #untill we remove the character which we get found as repeated
            # abcbd - for this ex.
            #window will get till abc, noww b occured, we want to start new window'
            #we have to remove all left chars untill b, so we can have new window from c
            #where we can have no repeatation
            substring.remove(s[left])
            left+=1
        substring.add(s[r])
        res = max(res, r-left+1)
        #current window length would be right index - left index + 1
    return res
print(lengthOfLongestSubstringSlidingWindow("abcbad"))

