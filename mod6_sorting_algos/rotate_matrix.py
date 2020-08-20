"""
Given an NxN matrix, rotate it by 90 degrees. You should perform this operation in-place, using only constant memory.

Example:
starting matrix:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
once rotated by 90 degrees, the matrix becomes:
 [
  [7, 4, 1]
  [8, 5, 2]
  [9, 6, 3]
]

Hint:
Is there an easy way to rotate a coordinate pair by 90 degrees?
"""


def rotate_matrix(matrix):
    mat_len = len(matrix)

    for row in range(mat_len):
        for col in range(row, mat_len):
            temporary = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temporary

        # this gives us: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    for row in range(mat_len):
        for col in range(mat_len // 2):
            temporary = matrix[row][col]
            print(matrix[row][mat_len - 1 - col])
            matrix[row][col] = matrix[row][mat_len - 1 - col]
            matrix[row][mat_len - 1 - col] = temporary

        # this gives us: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
