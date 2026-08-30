class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0]*n
        num1 = nums[:n-1]

        if n <= 3:
            return max(nums)

        dp[0] = num1[0]
        dp[1] = max(num1[0], num1[1])

        for i in range(2, n-1):

            dp[i] = max(dp[i-1], dp[i-2]+num1[i])

        num2 = nums[1:]
        dp1 = [0]*n
        dp1[0] = num2[0]
        dp1[1] = max(num2[0], num2[1])

        for i in range(2, n-1):
            
            dp1[i] = max(dp1[i-1], dp1[i-2]+num2[i])
        
        return max(dp[n-2], dp1[n-2])


        