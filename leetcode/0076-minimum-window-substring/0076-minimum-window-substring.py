class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n, m = len(s), len(t)

        if n < m:
            return ""

        left = 0 
        seen = Counter(t)
        count = Counter()
        
        res = s + "a"

        for right in range(n):

            if s[right] in seen:
                count[s[right]] += 1
   

            while count >= seen:

                if len(res) > right - left +1:
                    res = s[left: right +1]

                if s[left] in seen:
                    count[s[left]] -= 1

                left += 1

        return res if res != s + "a" else ""
    
    # s = aaaaa,  t = abc





        
        