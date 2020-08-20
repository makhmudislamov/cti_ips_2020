"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
"""


def minAddToMakeValid(S):
    if len(S) == 0:
        return 0
    open_par, closed_par = 0, 0
    for c in S:
        if c == '(':
            open_par += 1
        if c == ')':
            if open_par > 0:
                open_par -= 1
            else:
                closed_par += 1
    return open_par + closed_par
