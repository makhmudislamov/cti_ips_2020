"""
Given two strings s and t , write a function to determine if t is an anagram of s.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Note:
You may assume the string contains only lowercase letters.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution?
"""


def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    for char in s:
        print(char)
        if char not in t:
            return False
    for char in t:
        if char not in s:
            return False
    return True
