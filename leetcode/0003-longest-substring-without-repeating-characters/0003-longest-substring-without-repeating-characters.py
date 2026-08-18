class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        seen = Counter()
        left = 0
        for i in range(len(s)):

            seen[s[i]] +=1
            if seen[s[i]] == 2:
                while seen[s[i]] == 2:
                    seen[s[left]] -=1
                    left +=1
        
            ans = max(ans, i-left +1)
        return ans

               





        