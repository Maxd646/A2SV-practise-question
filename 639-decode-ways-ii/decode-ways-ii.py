class Solution:
    def numDecodings(self, s: str) -> int:

        mod = (10**9 + 7)
        n = len(s)

        if not s or s[0] == "0":

            return 0

        dp  = [0]*(n+1)
        dp[0] = 1

        if s[0] == "*":
            dp[1] = 9
        else:
            dp[1] = 1
        
        for i in range(2, n+1):

            one = s[i-1:i]
            two = s[i-2:i]

            if one  == "*":
                dp[i] += dp[i-1] *9
            elif one != "0":
                dp[i] += dp[i-1]
            
            if two == "**":
                dp[i] += 15 * dp[i-2]

            elif two[0] == "*":

                if "0" <= two[1] <= "6":
                    dp[i] += 2 *dp[i-2]

                else:
                    dp[i] += dp[i - 2]

            elif two[1] == "*":

                if two[0] == "1":
                    dp[i] += 9 * dp[i - 2]

                elif two[0] == "2":
                    dp[i] += 6 * dp[i - 2]

            elif 10 <= int(s[i-2:i]) <= 26:
                
                dp[i] += dp[i-2]

            dp[i] %= mod
                
        return dp[n]