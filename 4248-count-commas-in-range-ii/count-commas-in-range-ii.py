class Solution:
    def countCommas(self, n: int) -> int:
        total  = 0
        if n >= 10**3:
            total += min(n, 10**6-1) -999
        if n >= 10**6:
            total += (min(n, 10**9 -1) - 10**6 +1)*2
        if n >= 10**9:
            total += (min(n, 10**12 -1)- 10**9 +1)*3
        if n >= 10**12:
            total += (min(n, 10**15 -1) - 10**12+ 1)*4
        if n >= 10**15:
            total += (min(n , 10**18 -1) - 10**15 +1)*5
        return total

        