"""
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example:
>> arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
>> single_number(arr) # returns 4

OG Platform:  https://www.interviewbit.com/problems/single-number-ii/ 
"""


def single_number(nums):
    ans = 0
    for i in range(0, 32):
        count = 0
        for a in nums:
            if ((a >> i) & 1):
                count += 1
        ans |= ((count % 3) << i)
    return convert(ans)


def convert(x):
    if x >= 2**31:
        x -= 2**32
    return x
