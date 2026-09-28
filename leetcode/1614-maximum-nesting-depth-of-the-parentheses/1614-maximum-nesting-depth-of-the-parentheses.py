class Solution:
    def maxDepth(self, s: str) -> int:


        ans = 0
        maxx = 0
        for ch in s:

            if ch == "(":

                ans += 1
                maxx = max(ans, maxx)
                continue

            if ch == ")":
                ans -= 1

        return maxx
            
        