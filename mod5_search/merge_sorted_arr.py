"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.


Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


def merge_sorted_list(nums1, nums2):
    # modify num1 in-place
    nums1_indx = 0
    nums2_indx = 0

    while nums2_indx < len(nums2):
        if nums2[nums2_indx] <= nums1[nums1_indx] or nums1[nums1_indx] == 0:
            nums1.insert(nums1_indx, nums2[nums2_indx])
            nums1.pop()
            nums2_indx += 1
        else:
            nums1_indx += 1
