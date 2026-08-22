class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n %(sum(map(int, str(n)))+ math.prod(map(int, str(n)))) == 0
        