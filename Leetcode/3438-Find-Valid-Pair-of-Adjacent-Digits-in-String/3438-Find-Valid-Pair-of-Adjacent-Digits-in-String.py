# Find Valid Pair of Adjacent Digits in String
# Platform: LeetCode

class Solution:
    def findValidPair(self, s: str) -> str:
        Count=Counter(s)
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                if Count[s[i]]==int(s[i]) and Count[s[i+1]]==int(s[i+1]):
                    return s[i:i+2]
        return ""
# or
class Solution:
    def findValidPair(self, s: str) -> str:
        Count=Counter(s)
        res=""
        seen= set()
        j=0
        for ch, num in Count.items():
            if int(ch)==num:
                res+=ch
        if len(res)<2:
            return ""
        seen= set(res)
        found=False
        for i in range(len(s)-1):
            if s[i] in seen and s[i+1] in seen:
                seen.add(s[i:i+2])
        
        found =False
        for i in range(len(s)):
            if s[i:i+2] in seen and len(set(s[i:i+2]))==2:
                found=True
                return s[i:i+2]
        if not found:
            return ""
