class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        dist = 1
        maxx = 0
        index = seats.index(1)
        index2 = seats[::-1].index(1)

        for val in seats:
            if val == 1:
                maxx = max(dist, maxx)
                dist = 1
            else:
                dist  += 1
    
        return max([maxx//2, index, index2])


        