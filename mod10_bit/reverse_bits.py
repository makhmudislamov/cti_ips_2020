"""
Given an integer n, reverse its first 32 bits, and return the reversed-bit integer.
0 <= n <= 2^32 - 1
Example:
5 (00000000000000000000000000000101) ==> 2684354560 (10100000000000000000000000000000)
"""


def reverse_bits(num):
    nn = 0
    count = 0
    while count < 32:
        v = num % 2
        num = num >> 1
        nn = (nn << 1) + v
        count += 1

    return nn
