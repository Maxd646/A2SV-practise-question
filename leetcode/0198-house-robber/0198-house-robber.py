class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo =  {}
        def maxval(i):
            if i== 0:
                return nums[i]
            if i ==1:
                return max(nums[1], nums[0])
            if i not in memo:
                memo[i] = max(maxval(i-1), maxval(i-2)+nums[i])
            return memo[i]
        return maxval(n-1)

            
        
        