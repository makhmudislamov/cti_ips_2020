"""
You recently learned a new way to sort an array of numbers in your algorithms course. The algorithm sorts an array of numbers by repeatedly performing the Delete-and-Append operation. The Delete-and-Append operation consists of three steps:
Choose an element from the array.
Delete the chosen element from the array.
Append the chosen element to the end of the array.
Being a curious student, you wonder what is the minimum number of Delete-and-Append operations required to sort a given array.

Instructions:
Given an array of integers, find out the minimum number of Delete-Append operations that are required to make the array sorted. 

You can solve this problem in a number of ways. 
Hint 1: Could you somehow find out how many operations are necessary by looking at the already sorted version of the array?
Hint 2: Alternatively, it is possible to find out the minimum number of required operations without sorting the list?

Example:
[1, 5, 2, 4, 3, 6]; Starting array
[1, 5, 2, 3, 6, 4]; DA 4
[1, 2, 3, 6, 4, 5]; DA 5
[1, 2, 3, 4, 5, 6]; DA 6

Done! Took three operations.

Original site: https://open.kattis.com/problems/dasort 
"""
