class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        maxx = 1
        for i in range(1, len(s)):
            if ord(s[i])-1 == ord(s[i-1]):
                maxx+=1
            else:
                ans = max(maxx, ans)
                maxx = 1
        ans = max (maxx, ans)
        return ans


        
        