class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        def nCrmod(n, r):
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n // 2: r = n - r
            num, den = 1, 1
            for i in range(r):
                num = (num * (n - i)) % MOD
                den = (den * (i + 1)) % MOD
            return (num * pow(den, MOD - 2, MOD)) % MOD

        def count(total, blocks):
            if blocks <= 0 or total < blocks:
                return 0
            ans = 0
            for i in range(blocks + 1):
                
                nval = total - (i * limit) - 1
                rval = blocks - 1
                if nval < rval:
                    break
                
                term = (nCrmod(blocks, i) * nCrmod(nval, rval)) % MOD
                ans = (ans - term + MOD) % MOD if i % 2 else (ans + term) % MOD
            return ans

        result = 0
     
        for k in range(1, zero + 1):
            ways = count(zero, k)
            if not ways:
                continue
           
            result = (result + 2 * ways * count(one, k)) % MOD
            
            result = (result + ways * count(one, k - 1)) % MOD
          
            result = (result + ways * count(one, k + 1)) % MOD
            
        return result % MOD
