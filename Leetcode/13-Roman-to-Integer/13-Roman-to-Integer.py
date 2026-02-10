# Roman to Integer
# Platform: LeetCode

class Solution:
    def romanToInt(self, s: str) -> int:
        value={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500, "M":1000}
        total=0
        pre=0
        for char in reversed(s):
            val= value[char]
            if val<pre:
                total-=val
            else:
                total+=val
            pre=val
        return total
## or 
class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        seen={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500, "M":1000}
        j=len(s)-1
        found =False
        while j>0:
            if seen[s[j]]>seen[s[j-1]]:
                num+=seen[s[j]]-seen[s[j-1]]
                if j==1:
                    found=True
                j-=2
            else:
                num+=seen[s[j]]
                j-=1
        if found:
            return num
        else:
            return num+seen[s[0]]
        
                





        
