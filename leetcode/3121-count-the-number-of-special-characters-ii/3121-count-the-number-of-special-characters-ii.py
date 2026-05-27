class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower[ch] = i
            else:
                c = ch.lower()
                if c not in upper:
                    upper[c] = i

        ans = 0

        for c in lower:
            if c in upper and lower[c] < upper[c]:
                ans += 1

        return ans