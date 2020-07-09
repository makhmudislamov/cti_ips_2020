"""
Instructions from your teacher:
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false
Example 3:
Input: 9
Output: true
Example 4:
Input: 45
Output: false
"""


def power_of_three(n):
  # FOUND THIS HERE: https://www.geeksforgeeks.org/find-whether-given-integer-power-3-not/
    """ The maximum power of 3 value that  
     integer can hold is 1162261467 ( 3^19 ) ."""
    # if 1162261467 % n == 0:
    #   return True
    # return False

    # MY SOLUTION >> test at n = 243 was not passing because log_base_3 = 4.999999999999
    # getting log3(n)
    # log_base_3 = math.log(n, 3)
    # # check if log_base_3 is a whole num
    # if log_base_3 % 2 == 0 or (log_base_3 + 1) % 2 == 0:
    #     return True
    # return False

    # ANOTHER SOLUTION I MADE:

    while n > 1:
      n /= 3

    if n == 1:
        return True
    return False
