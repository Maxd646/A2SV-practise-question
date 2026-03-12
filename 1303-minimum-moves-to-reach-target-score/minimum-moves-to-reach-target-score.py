class Solution:
    def minMoves(self, n: int, D: int) -> int:
        ans=0
        while n>1:
            if D>0:
                if n%2==0:
                    n//=2
                    ans+=1
                    D-=1
                else:
                    n=n-1
                    ans+=2
                    n//=2
                    D-=1
            else:
                return ans+ n-1
        return ans
            


        