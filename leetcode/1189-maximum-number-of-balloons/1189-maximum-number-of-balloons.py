class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a, b, l, n, o = text.count("a"), text.count("b"), (text.count("l"))//2, text.count("n"), (text.count("o"))//2
        return min([a, b, l, n, o])
        # nnnn
        