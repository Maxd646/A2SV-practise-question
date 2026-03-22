class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans= []
        i, j= 0, len(s)
        for ch in s:
            if ch=="I":
                ans.append(i)
                i+=1
            else:
                ans.append(j)
                j-=1
        return ans + [j]
        