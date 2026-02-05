# Find Duplicate File in System
# Platform: LeetCode
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result=[]
        seen=defaultdict(list)
        for ch in paths:
            arra=ch.split()
            root=arra[0]
            for cha in arra[1:]:
                i=j=0
                name=title=""
                block=False
                while i<len(cha):
                    if cha[i]=="(":
                        j=i
                        title=cha[0:j]
                        block=True
                    elif block and cha[i]==")":
                        name=cha[j+1:i]
                    i+=1
                seen[name].append(root+"/"+title)

        for num in seen.values():
            if len(num)>1:
                result.append(num)
        return result

