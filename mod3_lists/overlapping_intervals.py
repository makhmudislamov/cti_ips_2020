"""
Given a collection of intervals, merge all overlapping intervals.

These intervals are sorted by the starting index; [[1, 4], [2, 3]] is fine but [[2, 3], [1, 4]] is not.

For example:
Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""


def merge_overlapping_intervals(intervals):
  if len(intervals) < 2:
      return intervals

  index = 0
  while index < len(intervals) - 1:
    #   check if the last item of an array is greater or equal to the first item of next array
      if intervals[index][1] > intervals[index + 1][0]:
          del intervals[index][1]
          del intervals[index + 1][0]
          intervals[index].extend(intervals[index + 1])
          del intervals[index + 1]
      else:
          index += 1
  return intervals
