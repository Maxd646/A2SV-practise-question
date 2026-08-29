class Solution:
    def minMoves(self, target: int, k: int) -> int:
        ans = 0
        n = target
        while n > 1:

            if k>0:
        
                if n%2 == 0:
                    n //= 2
                    ans += 1
                    k -= 1
                    continue
                
                n -= 1
                n //= 2
                k -= 1
                ans += 2
                continue 

            return ans + n-1

        return ans
            
                


            
            

        