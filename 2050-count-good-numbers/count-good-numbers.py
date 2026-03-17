class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod =(10**9+7)
        if n%2==0:
            c=n//2
            return (pow(5, c, mod)*pow(4, c, mod))%mod
        else:
            c=(n//2)+1
            b=n//2
            return (pow(4, b, mod)*pow(5, c, mod))%mod


        

        
