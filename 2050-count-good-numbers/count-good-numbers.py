class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod= 10**9+7
        def count(x , n) :
            print("state", x, n)
            if n == 0 :
                print("a", 1)
                return 1
            if n == 1 :
                print("b", x)
                return x
            a = count(x, n//2)
            if n % 2!=0:
                print(x, a, (a * a * x) % mod)
                return (a * a * x) % mod
            print(x, a, (a * a ) % mod)
            return (a * a) % mod        

        ans = count(5, (n +1)// 2 )
        ans *= count(4, n//2) 

        return ans  % mod
        
