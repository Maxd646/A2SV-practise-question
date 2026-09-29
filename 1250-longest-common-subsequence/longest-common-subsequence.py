class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        dp = [[0]* (n+1) for _ in range(m+1)]
        maxx = 0

        for i in range(m):

            for j in range(n):

                if text2[i] == text1[j]:

                    dp[i+1][j+1] = dp[i][j] + 1

                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

                maxx = max(maxx, dp[i+1][j+1])


        return maxx

        





        

        