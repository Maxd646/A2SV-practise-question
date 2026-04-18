class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(set(nums))<2:
            return 0
        maxN= -float("inf")
        nums.sort()
        for i in range(1, len(nums)):
            maxN= max(nums[i]-nums[i-1], maxN)
        return maxN


        
        