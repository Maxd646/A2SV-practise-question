class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n=s.count("1")
        return True if "1"*n in s else False