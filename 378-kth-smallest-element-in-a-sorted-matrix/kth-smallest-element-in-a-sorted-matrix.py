class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])
        return heapq.nsmallest(k, heap)[-1]
                
       

        