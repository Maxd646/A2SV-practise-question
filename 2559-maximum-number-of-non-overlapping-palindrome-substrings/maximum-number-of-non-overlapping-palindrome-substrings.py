class Solution:
    def maxPalindromes(self, s: str, m: int) -> int:
        
        n = len(s)

        dp = [[False]*n for _ in range(n)]

        for i in range(n):

            dp[i][i] = True
        
        for i in range(n-1):
            
            if s[i] == s[i+1]:
                dp[i][i+1] = True

        for i in range(3, n+1):
            for j in range(n-i+1):

                k = j + i -1

                if s[j] == s[k] and dp[j+1][k-1]:

                    dp[j][k] = True

        d = [0] * (n + 1)

        for i in range(1, n + 1):


            d[i] = d[i - 1]

            
            for left in range(i):

                length = i - left

                if length >= m and dp[left][i - 1]:

                    d[i] = max(d[i],d[left] + 1)
                   
        return d[n]
        
        
        