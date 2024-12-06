'''
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''
from collections import defaultdict

# one more easy task would be we use sorted word as key 
def groupAnagrams1(strs):
    # Create a dictionary to hold our anagram groups
    anagrams = defaultdict(list)
    
    # Iterate over each word in the list
    for word in strs:
        # Sort the word and use it as the key
        sorted_word = ''.join(sorted(word))
        # Add the original word to the corresponding list in the dictionary
        anagrams[sorted_word].append(word)
        #for the anagrams key would be same as sorted word is same for anagrams
    
    # Return the values of the dictionary as a list of lists
    return list(anagrams.values())
# this would be m*(n*logn) (n*logn) for each word we sort and we do that 4 m times
# where m is length of array and n is length of word

# we have to count the characters in each string
# and group the strs which's character count matches
# one way of doing this is making 26 0s list
# and setting character count accordingly ascii nums(a1-z26)
# not that count list will work as pattern for that word
# for anagrams that pattern will be same and we will make hashmap
# we use pattern as keys and words matching that pattern(anagrams) as values
# values of dict will be list type as list 

def groupAnagrams2(strs):
    res = defaultdict(list)
    for word in strs:
       count = [0]*26
       for c in word:
          count[ord(c)-ord('a')]+=1
          # as ascii value would be 64 and so on...
          # but we have to represent them 0-25 as in count list
          # that's why we subtract from base value(a's ascii value)
       res[tuple(count)].append(word) 
       #we cannot use list as key for dictionary as list are mutable that's why tuple
    return list(res.values()) 
#it would be m*n, m 4 first iteration(loop) length of strs
#and n 4 2nd iter length of string


import time
import random
import string

def generate_random_strings(num_strings, min_len=1, max_len=10):
    random_strings = []
    for _ in range(num_strings):
        length = random.randint(min_len, max_len)
        random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
        random_strings.append(random_string)
    return random_strings

# Generate an array of 100 random strings
rand_strs = generate_random_strings(100, 5, 40)

t1 = time.perf_counter()
print(groupAnagrams1(rand_strs))
t2 = time.perf_counter()
print(format(t2-t1, '0.8f'))

t3 = time.perf_counter()
print(groupAnagrams2(rand_strs))
t4 = time.perf_counter()
print(format(t4-t3, '0.8f'))