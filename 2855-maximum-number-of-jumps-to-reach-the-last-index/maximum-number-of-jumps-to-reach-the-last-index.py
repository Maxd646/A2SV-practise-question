class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i):
            if i == n - 1:
                return 0

            best = float('-inf')

            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    res = dfs(j)
                    if res != float('-inf'):
                        best = max(best, 1 + res)

            return best

        ans = dfs(0)
        return ans if ans != float('-inf') else -1