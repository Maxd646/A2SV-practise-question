# Word Pattern
# Platform: LeetCode
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        nums=s.split()
        if len(nums)!=len(pattern):
            return False
        seen ={}
        seen2={}
        for i in range(len(nums)):
            p=pattern[i]
            n=nums[i]
            if p in seen and seen[p]!=n:
                return False
            if n in seen2 and seen2[n]!=p:
                return False
            seen[p]=n
            seen2[n]=p
        return True
