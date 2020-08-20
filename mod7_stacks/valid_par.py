"""
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Original Site:  https://www.interviewbit.com/problems/generate-all-parentheses/ 
"""


def valid(parentheses):
    pars = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    if len(parentheses) % 2 != 0:
        return False

    stack = []

    for par in parentheses:
        if par in pars:
            stack.append(pars[par])
        else:
            if len(stack) == 0:
                return False
            current_par = stack.pop()
            if current_par != par:
                return False

    if not stack:
        return True
    return False
