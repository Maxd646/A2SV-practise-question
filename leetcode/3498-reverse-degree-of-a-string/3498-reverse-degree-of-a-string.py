class Solution:
    def reverseDegree(self, s: str) -> int:

        ans = 0 
        
        for i in range(len(s)):

            ans += (123 - ord(s[i]))*(i+1)
           

        return ans