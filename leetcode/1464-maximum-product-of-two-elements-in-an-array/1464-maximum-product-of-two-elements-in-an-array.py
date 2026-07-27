class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(nums)):
            if nums[i]>first:
                second = first
                first = nums[i]
            elif nums[i]>second:
                second = nums[i]
        return (second -1)*(first-1)


        