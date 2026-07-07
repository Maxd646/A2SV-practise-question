class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = ""
        n = str(n)
        for ch in n:
            if ch != "0":
                num+=ch
        summ = sum(map(int, str(num)))
        if num:
            return summ*int(num)
        return 0

        