class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
       
        if n < 2:
            return s
        dp = [[False]*n for _ in range(n)]

        start, maxlen = 0, 1

        for i in range(n):

            dp[i][i] = True

        for i in range(n-1):

            if s[i] == s[i+1]:

                dp[i][i+1] = True

            if dp[i][i+1]:

                start, maxlen = i, 2

        for i in range(3, n+1):

            for j in range(n-i+1):

                k = i+j-1

                if s[j] == s[k] and dp[j+1][k-1]:

                    dp[j][k] = True
                    start, maxlen = j, i

        return s[start:start+maxlen]


        