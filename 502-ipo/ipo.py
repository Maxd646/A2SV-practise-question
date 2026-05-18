from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        seen = sorted([capital[i], profits[i]] for i in range(len(capital)))
        
        maxx = []
        i = 0
        n = len(seen)

        for _ in range(k):
            while i < n and seen[i][0] <= w:
                heapq.heappush(maxx, -seen[i][1])
                i += 1

            if not maxx:
                break
           
            w += -heapq.heappop(maxx)

        return w