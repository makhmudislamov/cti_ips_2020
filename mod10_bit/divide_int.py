"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Example 2:
Input: dividend = 7, divisor = -3
Output: -2
"""


def divide(dividend, divisor):
    sign = -1 if ((divisor > 0) ^ (dividend > 0)) else 1

# prevent overflow
    if dividend == -2**31 and divisor == -1:
        return 2**31-1

    dividend = abs(dividend)
    divisor = abs(divisor)

    res = 0
    while divisor <= dividend:
        div = divisor
        tmp = 1
        while(div << 1 <= dividend):
            tmp <<= 1
            div <<= 1
        dividend -= div
        res += tmp
    return res*sign


testX = 4
testY = 1
testResult = divide(testX, testY)
print(testResult)
