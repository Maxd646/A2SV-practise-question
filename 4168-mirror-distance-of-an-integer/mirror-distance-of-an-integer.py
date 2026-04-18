class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = n
        ans =0
        while n>0:
            ans = ans*10+n%10
            n//=10
        return abs(ans-a)


  
        