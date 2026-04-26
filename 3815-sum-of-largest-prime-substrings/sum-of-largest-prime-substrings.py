class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(num):
            if num < 2: return False
            if num == 2 or num == 3: return True
            for i in range(2, int(num**0.5) + 1, 1):
                if num % i == 0 :
                    return False
            return True

        seen = set()
        n = len(s)
      
        for i in range(n):
            for j in range(i + 1, n + 1):
                val = int(s[i:j])
                if val not in seen and is_prime(val):
                    seen.add(val)
        
        largest= sorted(list(seen))
        return sum(largest[-3:])
