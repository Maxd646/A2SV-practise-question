class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        maxdp = [0] * n
        mindp = [0] * n

        maxdp[0] = nums[0]
        mindp[0] = nums[0]

        ans = nums[0]

        for i in range(1, n):
            
            x = nums[i]

            maxdp[i] = max(x, x * maxdp[i - 1], x * mindp[i - 1])

            mindp[i] = min(x, x * maxdp[i - 1], x * mindp[i - 1])

            ans = max(ans, maxdp[i])

        return ans
