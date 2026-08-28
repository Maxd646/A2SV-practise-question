class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:


        n, m = len(grid), len(grid[0])
        ans = float("inf")
        memo = {}

        def dp(i, j):
            
            nonlocal ans

            if i == n - 1 and j == m - 1:
                return grid[i][j]

            if i >= n or  j>= m:
                return float("inf")

            if (i, j) not in memo:
                memo[(i, j)] = grid[i][j] +  min(dp(i, j+1), dp(i+1, j))

            return memo[(i, j)]

        return dp(0, 0)