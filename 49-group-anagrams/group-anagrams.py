class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen= defaultdict(list)
        for ch in strs:
            nn= list(ch)
            nn.sort()
            seen["".join(nn)].append(ch)
        result=  list(seen.values())
        return result