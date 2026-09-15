class Solution:
    def checkPartitioning(self, s: str) -> bool:

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        for i in range(3, n + 1):
            for j in range(n - i + 1):

                k = j + i - 1

                if s[j] == s[k] and dp[j + 1][k - 1]:
                    dp[j][k] = True

        for i in range(n - 2):
            for j in range(i + 1, n - 1):

                if dp[0][i] and dp[i + 1][j] and dp[j + 1][n - 1]:
                    return True

        return False