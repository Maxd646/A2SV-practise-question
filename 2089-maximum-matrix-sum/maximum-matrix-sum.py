class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        minn = float("inf")
        count = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    count += 1
                minn = min(minn, abs(val))

        if count % 2 != 0:
            total -= 2 * minn

        return total