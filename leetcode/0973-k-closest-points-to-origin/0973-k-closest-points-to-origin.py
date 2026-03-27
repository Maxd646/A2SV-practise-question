class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        seen= [[(x**2 + y**2)**0.5, [x, y]] for x, y in points]
        seen = sorted(seen)[:k]
        ans = []
        for point in seen:
            ans.append(point[1])
        return ans
        