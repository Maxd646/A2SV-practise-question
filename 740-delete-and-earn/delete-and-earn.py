class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        n = max(nums)
        m = min(nums)
        dp = [0]*(n+1)

        for num in nums:
            dp[num] += num

        if n-m <= 1:
            return max(dp)


        dp[m+1] = max(dp[m+1], dp[m])

        for i in range(m+2, n+1):

            dp[i] = max(dp[i-1], dp[i-2]+dp[i])

        return dp[n]

       
        

 

        