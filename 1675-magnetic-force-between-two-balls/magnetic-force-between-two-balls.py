class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_i(x):
            y = position[0]
            count = 1
            for i in range(1, len(position)):
                if position[i] - y >= x:
                    count += 1
                    y = position[i]
                if count >= m:
                    return True
            return False
        ans = 0
        l, r = 1, position[-1] - position[0]
        while l <= r:
            mid = (l + r) // 2
            if can_i(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
        