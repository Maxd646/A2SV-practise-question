class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:

        n = len(nums)
        dp = [0]*n
        dpmin = [0]*n

        dp[0] = nums[0]
        dpmin[0] = nums[0]

        
        for i in range(1, n):

            dp[i] = max(nums[i], nums[i] + dp[i-1])
            dpmin[i] = min(nums[i], nums[i]+ dpmin[i-1])
            

        return max(abs(min(dpmin)), max(dp))
        