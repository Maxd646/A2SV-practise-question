class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n <= 3:
            
            return max(nums)

        def dp(nums):

            m =  n-1
            dp = [0]*m

            if m <= 2:

                return max(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n-1):

                dp[i] = max(dp[i-1], dp[i-2]+nums[i])

            return dp[m-1]
        
        return max(dp(nums[1:]), dp(nums[:n-1]))
        