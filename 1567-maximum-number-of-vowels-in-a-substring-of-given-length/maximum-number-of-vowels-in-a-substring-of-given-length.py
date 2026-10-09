class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        ans = 0
        seen = set("aeiou")
        count = 0
        for i in range(k):
            count += 1 if s[i] in seen else 0
            
        ans = count

        for i in range(k, len(s)):

            count -= 1 if s[i-k] in seen else 0
            count += 1 if s[i] in seen else 0
            ans = max(ans, count)

        return ans 

            
        