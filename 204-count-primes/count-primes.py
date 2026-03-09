class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime =[True]*(n)
        p=2
        while p*p<n:
            if prime[p]:
                for i in range(p*p, n, p):
                    prime[i]=False
            p+=1
        return prime[2:].count(True)

        