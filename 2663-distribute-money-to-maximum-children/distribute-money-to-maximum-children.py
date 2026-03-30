class Solution:
    def distMoney(self, money: int, children: int) -> int:
        n= money
        m = children
        if n < m:
            return -1
        
        n -= m  
        
        maxx = n // 7
        
        if maxx == m and n % 7 == 0:
            return m
        
        if maxx== m - 1 and n % 7 == 3:
            return m - 2
        
        return min(maxx, m - 1)

