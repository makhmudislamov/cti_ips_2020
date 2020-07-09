"""
Instructions from your teacher:
Given an unsorted integer array, find the first missing positive integer.



Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time.
"""


def first_missing_positive_integer(integers):
    found_int = []

    for integer in integers:
        if integer < 0:
            continue
        if integer + 1 > len(found_int):
            extend_size = integer - len(found_int) + 1
            found_int.extend([False] * extend_size)
        found_int[integer] = True

    missing_int = 0
    for position in range(1, len(found_int)):
        if found_int[position] == False:
            missing_int = position
        return missing_int

    if missing_int == 0 and len(found_int) == 0:
        return 1
    elif missing_int == 0 and len(found_int) > 0:
        return len(found_int)
