class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minn = float("inf")
        ans = 0

        for num in prices:
            if num < minn:
                minn = num
            else:
                diff = num- minn
                ans = max(diff, ans)
        return ans
        