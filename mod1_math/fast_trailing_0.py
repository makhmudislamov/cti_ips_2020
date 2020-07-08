"""
Instructions from your teacher:
Below is the prompt for a stretch problem. This problem involves all the same operations you're used to, but with the added complexity of needing to solve it without brute-force (eg, you can't just calculate the factorial manually.)

Originally located here: https://www.interviewbit.com/problems/trailing-zeros-in-factorial/

Prompt

Given an integer n, return the number of trailing zeroes in n!.

Your solution should be in logarithmic time complexity.

For a hint, try looking at this spreadsheet, to see if you notice a pattern that can help you predict the number of trailing zeros. What happens as n rises? What are the transition points where the number of trailing zeros rises?
 
https://docs.google.com/spreadsheets/d/1C6ln6zfmG5Q92fHJosjZxe0WuSS0x_WThzBtc5_n6GA/edit#gid=0
"""


def fast_trailing_zero_factorial(n):

    return n


print("Enter number")
n = input()
n = int(n)
print("The number of trailing zeroes is " +
      str(fast_trailing_zero_factorial(n)))
