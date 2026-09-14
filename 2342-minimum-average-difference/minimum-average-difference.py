class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        ans = float("inf")
        index = 0
        n = len(nums)

        left = 0
        total = sum(nums)
        l = 0

        for i in range(len(nums)):

            left += nums[i]
            total -= nums[i]
            n -= 1
            l += 1
            diff = abs((left//l) - (total//n if n else 0))

            if diff < ans:
                ans = diff
                index = i
        

        return index



        