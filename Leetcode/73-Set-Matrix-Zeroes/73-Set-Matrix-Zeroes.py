# Set Matrix Zeroes
# Platform: LeetCode
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        seenx=set()
        seeny=set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    seenx.add(i)
                    seeny.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in seenx:
                    matrix[i][j]=0
                elif j in seeny:
                    matrix[i][j]=0
