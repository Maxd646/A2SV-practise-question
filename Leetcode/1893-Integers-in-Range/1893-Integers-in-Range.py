# Integers in Range
class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            Found = False
            for i, j in ranges:
                if i <= x <= j:
                    Found = True
                    break
            if not Found:
                return False
        return True
