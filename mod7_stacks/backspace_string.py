"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""


def compile(x):

    stack = []
    for y in x:
        if y == '#':
            if stack:
                stack.pop()
        else:
            stack.append(y)
    return stack


def backspaceCompare(String1, String2):

    return compile(String1) == compile(String2)
