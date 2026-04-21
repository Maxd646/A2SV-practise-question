from functools import lru_cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def df(i, j):
            if i == j:
                return nums[i]

            return max(
                nums[i] - df(i + 1, j),
                nums[j] - df(i, j - 1)
            )

        return df(0, n - 1) >= 0