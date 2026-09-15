class Solution:
    def minCut(self, s: str) -> int:

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

        d = [float("inf")] * (n + 1)
        
        d[n] = 0

        for start in range(n - 1, -1, -1):

            for end in range(start, n):

                if dp[start][end]:

                    d[start] = min(d[start], 1 + d[end + 1])

        return d[0]-1