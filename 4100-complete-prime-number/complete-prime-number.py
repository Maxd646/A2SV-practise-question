class Solution:
    def completePrime(self, num: int) -> bool:
        if num <2:
            return False
        def prime(num):
            if num<2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num%i==0:
                    return False
            return True

        s = str(num)
        for i in range(len(s)):
            if not prime(int(s[:i+1])):
                return False

            elif not prime(int(s[i:])):
                return False
        return True
        
        
        
        