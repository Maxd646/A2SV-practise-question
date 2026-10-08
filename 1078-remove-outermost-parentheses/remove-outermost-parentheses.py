class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        close = 0
        ans = ""

        for ch in s:

            if ch == "(":

                if close > 0:
                    ans += ch
                close += 1

            else:

                close -= 1

                if close>0:
                    ans += ch
                
        return ans 

            



             

            





        