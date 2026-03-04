# Minimum Value to Get Positive Step by Step Sum
# Platform: LeetCode
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        nums=accumulate(nums)
        aa=min(nums)
        return 1-aa if aa<0 else 1
    
