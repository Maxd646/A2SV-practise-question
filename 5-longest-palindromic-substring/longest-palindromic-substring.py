class Manacher:
    def __init__(self, s):
        self.t = '#' + '#'.join(s) + '#'
        n = len(self.t)
        self.p = [0] * n
        c = r = 0
        for i in range(n):
            if i < r:
                self.p[i] = min(r - i, self.p[2 * c - i])
            while i + self.p[i] + 1 < n and i - self.p[i] - 1 >= 0 and \
                  self.t[i + self.p[i] + 1] == self.t[i - self.p[i] - 1]:
                self.p[i] += 1
            if i + self.p[i] > r:
                c, r = i, i + self.p[i]

    def getLongest(self, i, is_odd):
        
        idx = 2 * i + 1 if is_odd else 2 * i
        return self.p[idx]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        mob = Manacher(s)
        n = len(s)
        maxLen = 1
        bestStart = 0

        for i in range(n):
           
            oddLen = mob.getLongest(i, 1)
            if oddLen > maxLen:
                maxLen = oddLen
                bestStart = i - maxLen // 2

          
            if i > 0:
                evenLen = mob.getLongest(i, 0)
                if evenLen > maxLen:
                    maxLen = evenLen
                    bestStart = i - maxLen // 2
        
        return s[bestStart: bestStart + maxLen]
