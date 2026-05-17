class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n  

        valid = {('0','0'), ('2','5'), ('5','0'), ('7','5')}

       
        for j in range(n):
            for i in range(j):
                if (num[i], num[j]) in valid:
                    
                    removed = 0

                    
                    removed += (n - j - 1)

                    
                    removed += (j - i - 1)

                    
                    ans = min(ans, removed)


        if '0' in num:
            ans = min(ans, n - 1)

        return ans