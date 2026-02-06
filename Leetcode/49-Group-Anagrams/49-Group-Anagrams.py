# Group Anagrams
# Platform: LeetCode
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs.sort()
        seen= defaultdict(list)
        for ch in strs:
            nn= list(ch)
            nn.sort()
            seen["".join(nn)].append(ch)
        result= [valu for ch, valu in seen.items()]
        return result      

