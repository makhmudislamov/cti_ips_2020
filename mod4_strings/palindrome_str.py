"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Examples:
"Race Car" # returns 1

"Race a Car" # returns 0

"otto" # returns 1

"A man, a plan, a canal, Panama." # returns 1
"""

import string


def isPalindrome(s):
    s = s.lower()
    s = s.translate(s.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")

    if s == s[::-1]:
        return True
    return False
