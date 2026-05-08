class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heapq.heappush(heap, -num)
        heapq.heapify(heap)
        while len(heap)>1:
            y = -(heapq.heappop(heap))
            x = -(heapq.heappop(heap))
            print(y, x)
            if x == y:
                continue
            else: 
                heapq.heappush(heap, -(y- x))
                heapq.heapify(heap)
        if heap:
            return abs(heap[-1])
        return 0

