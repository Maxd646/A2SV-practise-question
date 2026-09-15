class Solution:
    def partition(self, s: str) -> list[list[str]]:

        ans = []
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

        def dfs(start, end, path):

            if start == n:
                ans.append(path[:])
                return

            if end == n:
                return

            if dp[start][end]:
                dfs( end + 1,end + 1,path + [s[start:end + 1]])

            dfs(start, end + 1, path)

        dfs(0, 0, [])

        return ans