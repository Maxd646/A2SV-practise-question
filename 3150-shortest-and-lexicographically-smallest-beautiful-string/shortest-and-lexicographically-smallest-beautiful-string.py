class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        left = 0
        count = 0
        ans = ""
        for i in range(len(s)):

            if s[i] == "1":
                    count  += 1

            while count > k:

                if s[left] == "1":
                    count -= 1
                left += 1
            
            if count == k:

                while s[left] =="0":
                    left +=1
        
                curr = s[left:i+1]

                if not ans or len(ans)>len(curr) or (len(ans) == len(curr) and ans >curr):
                    ans = curr
   
        return ans
           

                




        