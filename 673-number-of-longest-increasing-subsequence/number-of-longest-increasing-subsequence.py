class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        dp = [1] * n
        count = [1] * n

        for i in range(n):

            for j in range(i):

                if nums[i] > nums[j]:

                    if dp[j] + 1 > dp[i]:

                        dp[i] = dp[j] + 1
                        count[i] = count[j]

                    elif dp[j] + 1 == dp[i]:

                        count[i] += count[j]
        print(dp)
        print(count)

        longest = max(dp)

        ans = 0
        for i in range(n):

            if dp[i] == longest:
                ans += count[i]

        return ans