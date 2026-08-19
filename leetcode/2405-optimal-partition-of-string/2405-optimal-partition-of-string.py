class Solution:
    def partitionString(self, s: str) -> int:

        ans = 0
        seen = set()
        
        for i in range(len(s)):
  
            if s[i] in seen:
                ans += 1
                seen.clear()

            seen.add(s[i])

        return ans+1
        