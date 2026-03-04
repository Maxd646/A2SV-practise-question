# Shifting Letters II
# Platform: LeetCode
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters="abcdefghijklmnopqrstuvwxyz"
        s=list(s)
        aa=[0]*(len(s)+1)

        for i, j, k in shifts:
            if j<len(aa)-1:
                aa[j+1]+=(1 if k==0 else -1)

            aa[i]-=(1 if k==0 else -1)
            
        aa=list(accumulate(aa))  
        ans=""
        for i in range(len(s)):
            ans+=letters[(aa[i]+letters.index(s[i]))%26]
        return ans
