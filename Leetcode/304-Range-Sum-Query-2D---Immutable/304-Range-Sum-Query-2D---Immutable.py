# Range Sum Query 2D - Immutable
# Platform: LeetCode
class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.summm = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                self.summm[i][j] = (matrix[i-1][j-1]+ self.summm[i-1][j]+ self.summm[i][j-1]- self.summm[i-1][j-1] )

    def sumRegion(self, row1, col1, row2, col2):
        print(self.summm)
        return ( self.summm[row2+1][col2+1]- self.summm[row1][col2+1] - self.summm[row2+1][col1]+ self.summm[row1][col1])
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

