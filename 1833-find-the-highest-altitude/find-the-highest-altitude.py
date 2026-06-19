class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=max(list(accumulate(gain))) 
        return a if a>0 else 0
        