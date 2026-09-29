class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = text.count(pattern[0])
        m = text.count(pattern[1])

        a1 = 0
        ans = 0
        
        if pattern[0] == pattern[1]:
            return n * (n + 1) // 2

        for ch in text:

            if ch == pattern[0]:
                a1 += 1

            elif ch == pattern[1]:
                ans += a1

        return ans + max(n, m)