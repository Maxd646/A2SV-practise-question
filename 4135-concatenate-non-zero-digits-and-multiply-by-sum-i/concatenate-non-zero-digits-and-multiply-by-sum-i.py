class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        summ = 0
        for y in str(n):
            if y != "0":
                summ+= int(y)
                x = x*10+int(y)
        return x*summ

        

        