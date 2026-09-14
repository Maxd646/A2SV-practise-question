class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:


        x1 = min (ax2, bx2)
        x2 = max(ax1, bx1)
        y1 = min (ay2, by2)
        y2 = max(ay1, by1)

        total = (abs(ax2-ax1))*(abs(ay2-ay1)) + (abs(bx2-bx1))*(abs(by2-by1))

        if not (ax1 < bx2 and bx1 < ax2 and ay1 < by2 and by1 < ay2):
            return total

        return  total - (abs(x2 - x1)* (abs(y2-y1)))




       

        