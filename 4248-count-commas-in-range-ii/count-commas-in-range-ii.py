class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        m = 1000

        while m <= n:

            ans += n-m +1

            m *= 1000

        return ans 

        
        