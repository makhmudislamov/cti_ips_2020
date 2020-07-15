"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Examples:

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


def find_index(sorted_list, target):
  start = 0
  end = len(sorted_list)

  while start < end:
    pivot = start + (end - start) // 2

    if sorted_list[pivot] < target:
      start = pivot + 1
      # print(sorted_list[start])
    else:
      end = pivot

  return start
