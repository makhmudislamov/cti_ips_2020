"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Input
The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Sample
Input#1
T = [73, 74, 75, 71, 69, 72, 76, 73]
Output#1
[1, 1, 4, 2, 1, 1, 0, 0]
"""


def dailyTemperatures(dailyTemps):
    stack = []
    stack.append(0)
    ans = [0]*len(dailyTemps)
    for i in range(1, len(dailyTemps)):
        top = stack[-1]
        while dailyTemps[i] > dailyTemps[top]:
            ans[top] = i-top
            stack.pop()
            if len(stack) > 0:
                top = stack[-1]
            else:
                break
        stack.append(i)
    return ans
