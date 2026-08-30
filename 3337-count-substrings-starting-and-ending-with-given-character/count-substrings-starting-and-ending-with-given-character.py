
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        ans = 0

        for ch in s:
            if ch == c:
                count += 1
                ans += count

        return ans

