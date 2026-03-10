class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        N = zero + one + 5

        fact = [1]*(N)
        invfact = [1]*(N)

        for i in range(1, N):
            fact[i] = fact[i-1]*i % MOD

        invfact[N-1] = pow(fact[N-1], MOD-2, MOD)

        for i in range(N-2, -1, -1):
            invfact[i] = invfact[i+1]*(i+1) % MOD

        def nCr(n,r):
            if r < 0 or r > n:
                return 0
            return fact[n]*invfact[r]%MOD*invfact[n-r]%MOD

        def count(total, blocks):
            if blocks <= 0 or total < blocks:
                return 0

            ans = 0
            for i in range(blocks+1):
                nval = total - i*limit - 1
                rval = blocks - 1

                if nval < rval:
                    break

                term = nCr(blocks,i)*nCr(nval,rval)%MOD

                if i % 2:
                    ans = (ans - term) % MOD
                else:
                    ans = (ans + term) % MOD

            return ans

        res = 0

        for k in range(1, zero+1):
            ways = count(zero,k)
            if not ways:
                continue

            res = (res + 2*ways*count(one,k))%MOD
            res = (res + ways*count(one,k-1))%MOD
            res = (res + ways*count(one,k+1))%MOD

        return res %MOD