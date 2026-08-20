class Solution:
    def minDeletions(self, s: str) -> int:

        seen = Counter(s)
        used = set()
        ans = 0

        for ch, fre in seen.items():
            
            while fre in used and fre> 0:
                fre -=1
                ans +=1
            used.add(fre)

        return ans


       


        

        


        