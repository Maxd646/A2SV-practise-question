class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            pro = 1
            x = str(n)
            for i in range(len(x)):
                pro *= int(x[i])
            if int(pro)%t ==0:
                return n
            n += 1
        
        