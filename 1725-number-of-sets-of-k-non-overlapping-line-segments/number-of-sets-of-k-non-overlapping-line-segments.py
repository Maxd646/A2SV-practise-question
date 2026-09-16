class Solution:

    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [1] * n

        prefix = [0] * (n + 1)

        for j in range(n):
            prefix[j + 1] = (prefix[j] + dp[j]) % mod

        for _ in range(k):
            dp[0] = 0

            for j in range(1, n):
                dp[j] = (dp[j - 1] + prefix[j]) % mod

            for j in range(n):
                prefix[j + 1] = (prefix[j] + dp[j]) % mod
                
        return dp[n - 1]