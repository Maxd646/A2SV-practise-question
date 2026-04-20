class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n):
            if colors[0]!= colors[n-1-i] or colors[i]!= colors[n-1]:
                return n-1-i





        