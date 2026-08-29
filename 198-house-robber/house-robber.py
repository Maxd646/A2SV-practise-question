class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        memo =  {}

        def maxval(i):

            if i== n-1:
                return nums[i]

            if i == n-2:
                return max(nums[n-1], nums[n-2])

            if i not in memo:
                memo[i] = max(maxval(i+1), maxval(i+2)+nums[i])

            return memo[i]

        return maxval(0)

            
        
        