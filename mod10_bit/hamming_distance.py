"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


def hammingDistance(x, y):
    res = 0
    while x or y:
        if (x & 1) ^ (y & 1) == 1:
            res += 1
        x >>= 1
        y >>= 1
    return res


testX = 4
testY = 1
testResult = hammingDistance(testX, testY)
print(testResult)
