# Remove Comments
# Platform: LeetCode

class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        block=False
        result=[]
        new=""
        for ch in source:
            i=0
            while i<len(ch):
                if not block:
                    if i<len(ch)-1 and ch[i:i+2]=="/*":
                        block=True
                        i+=2
                    elif i<len(ch)-1 and ch[i:i+2]=="//":
                        i+=2
                        break
                    else:
                        new+=ch[i]
                        i+=1
                else:
                    if i+1<len(ch) and ch[i:i+2]=="*/":
                        block=False
                        i+=2
                    else:
                        i+=1
            if not block and new:
                result.append(new)
                new=""
        return result

