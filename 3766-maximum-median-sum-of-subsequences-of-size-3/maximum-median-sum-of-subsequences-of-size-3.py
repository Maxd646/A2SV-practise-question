class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        ans = 0

        left, right = 0, n-1

        while left <= right:

            ans += nums[right-1]
            left += 1
            right -= 2

        return ans 
        