# Rotate Image
# Platform: LeetCode
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        for i in range(len(matrix[0])):
            for j in range(1+i, len(matrix)):
                matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]

        for ch in matrix:
            ch.reverse()
