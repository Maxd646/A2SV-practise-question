class Solution:
    def maxProduct(self, n: int) -> int:
        seen = list(map(int, str(n)))
        first, second = 0, 0
        for i in range(len(seen)):
            if seen[i]>first:
                second = first
                first = seen[i]
            elif seen[i]>second:
                second = seen[i]
        return second * first
        
        