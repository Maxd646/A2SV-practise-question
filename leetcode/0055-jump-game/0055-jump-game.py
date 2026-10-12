class Solution:
    def canJump(self, nums: list[int]) -> bool:


        n = len(nums)
        dp = [False] *(n)
        dp[0] = True

        for i in range(n):

            if dp[i] == True and i + nums[i] >= n-1:
                return True

            if dp[i] == True:
                
                for j in range(i, nums[i]+i+1):
                    dp[j] = True

        return dp[n-1]


        


        