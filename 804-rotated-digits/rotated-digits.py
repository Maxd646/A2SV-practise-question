class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans =0
        seen =set([2,5,9, 6])
        invalid =set([3, 4, 7])
        for i in range(1, n+1):
            x = str(i)
            yes = False
            for ch in x:
                if int(ch) in invalid:
                    break
                elif int(ch) in seen:
                    yes = True
            else:
                if yes:
                    ans+=1
        return ans
        
        