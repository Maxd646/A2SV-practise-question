class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(n):
            if n == 2:
                return 2
            if n == 1:
                return 1
            if n not in memo:
                memo[n] = dp(n-1) + dp(n-2)
    
            return memo[n]
        return dp(n)
        