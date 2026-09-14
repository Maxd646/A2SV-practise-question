class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:


        summ = sum(nums)
        n = len( nums)
        left = 0
        ans = 0

        for i in range(n-1):

            left += nums[i]
            summ -= nums[i]

            if left >= summ:

                ans += 1

        return ans 


        