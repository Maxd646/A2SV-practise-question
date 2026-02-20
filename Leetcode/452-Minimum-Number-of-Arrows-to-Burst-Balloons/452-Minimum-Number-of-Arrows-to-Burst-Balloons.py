# Minimum Number of Arrows to Burst Balloons
# Platform: LeetCode
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[1])
        end= points[0][1]
        print(points)
        count=1
        for i in range(len(points)):
            if points[i][0]>end:
                count+=1
                end=points[i][1]
        return count
