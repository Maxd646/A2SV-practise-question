class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxx = 0
        left = 0
        summ = 0
        for i in range(len(s)):
            summ += abs(ord(s[i])-ord(t[i]))
            print(summ)
            while summ>maxCost:
                summ -= abs(ord(s[left])-ord(t[left]))
                left += 1
            maxx = max(maxx, i-left+1)
        return maxx
            

