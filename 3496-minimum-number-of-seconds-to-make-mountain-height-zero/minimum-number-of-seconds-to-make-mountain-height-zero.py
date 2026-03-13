class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxWorkerTimes = max(workerTimes)
        l, r, ans = (1, maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2, 0,)
        
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for t in workerTimes:
                work = mid // t
               
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2)
                cnt += k
            if cnt >= mountainHeight:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
        
        