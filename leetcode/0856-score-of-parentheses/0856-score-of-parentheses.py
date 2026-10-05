class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        ans = 0
        n = 0

        for i in range(len(s)):

            if s[i]== "(":
                n += 1

            else:
                n -= 1

                if s[i-1] == "(":
                    ans += 2**n

        return ans 

    




            

        
        