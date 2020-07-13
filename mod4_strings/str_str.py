"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. 

This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack, needle):
    if not haystack:
        return 0

    start = 0
    end = len(needle)
    while end < len(haystack) + 1:
        substring = haystack[start:end]
        print(substring)
    if substring != needle:
        start += 1
        end += 1
    else:
        return start

    return -1
