class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n= len(s1)
        m=len(s2)
        if n>m:
            return False
        count=Counter(s1)
        seen=Counter(s2[:n])
        if count==seen:
            return True
        left=0
        for i in range(n, m):
            seen[s2[i]]+=1
            seen[s2[left]]-=1
            left+=1
            if seen[s2[left]]==0:
                del seen[s2[left]]
            if seen==count:
                # m
                return True
        return False


        