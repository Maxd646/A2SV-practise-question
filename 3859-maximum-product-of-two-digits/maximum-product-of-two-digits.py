class Solution:
    def maxProduct(self, n: int) -> int:
        num = sorted(map(int, list(str(n))), reverse = True)
        return num[0]*num[1]
        