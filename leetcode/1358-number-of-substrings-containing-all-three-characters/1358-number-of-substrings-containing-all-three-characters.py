class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1] * 3
        total = 0

        for i in range(len(s)):
            last[ord(s[i]) - ord("a")] = i
            total += 1 + min(last)

        return total