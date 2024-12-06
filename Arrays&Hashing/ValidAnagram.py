'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
#we sort the string and compare it

def isAnagramUsingSorting(string1: str, string2: str) -> bool:
    return sorted(string1) == sorted(string2)

#sorting will be time O(nlogn) and o(1) space

#using hashmap
def isAnagramusingHashmap(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    s1_set = dict()
    s2_set = dict()
    for i in range(len(string1)):
        s1_set[string1[i]] = 1+s1_set.get(string1[i], 0) 
        s2_set[string2[i]] = 1+s2_set.get(string2[i], 0)
        #get function on hashmap return default value for key, if didn't found
    for char in s1_set:
        if s1_set[char] != s2_set.get(char, 0):
            return False
    return True        
#this is O(S+T+S) = O(N) where S, T, N length of string time and O(N)space
from collections import Counter
#using python in-built functions advantage for counting
def isAnagramusingInBuiltPyFunct(string1: str, string2: str) -> bool:
    return Counter(string1) == Counter(string2)
    #this function will do exactly the job which above function did

import time
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate a random string of length 10,000
string1 = generate_random_string(500)
string2 = generate_random_string(500)

t1 = time.perf_counter()
print(isAnagramusingHashmap(string1, string1))
t2 = time.perf_counter()
print(format(t2-t1, '0.8f'))

t3 = time.perf_counter()
print(isAnagramUsingSorting(string1, string1))
t4 = time.perf_counter()
print(format(t4-t3, '0.8f'))

t5 = time.perf_counter()
print(isAnagramusingInBuiltPyFunct(string1, string1))
t6 = time.perf_counter()
print(format(t6-t5, '0.8f'))
