class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        memo = {}
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        def dp(i, j):

            if i>= n or j>= m:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if i == n-1 and j == m-1:
                return 1

            if (i, j) not in memo:
                memo[(i, j)] = dp(i, j+1) + dp(i+1, j)

            return memo[(i, j)]
            
        return dp(0, 0)
