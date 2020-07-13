"""
Instructions from your teacher:
Given an array with three integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] 

You can assume the array is sorted.
Example
Given [1, 2, 3]

Output return: [2, 1, 3]
"""


def wave_array_3(integers):
    # iterate throught the array
    # shuffle every other elements
    index = 0
    while index < len(integers) - 1:
        # print(integers[index])
        if integers[index] <= integers[index + 1]:
            integers[index], integers[index +
                                      1] = integers[index + 1], integers[index]
            index += 2
    return integers
