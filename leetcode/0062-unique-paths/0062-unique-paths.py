class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}
        @lru_cache(None)
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if i == m -1 and j == n-1:
                return 1
            return dp(i, j+1) + dp(i+1, j)
        return dp(0, 0)

        