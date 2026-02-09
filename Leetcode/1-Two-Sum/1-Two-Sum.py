# Two Sum
# Platform: LeetCode
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen= dict()
        for i in range(len(nums)):
            num= target-nums[i]
            if num in seen:
                return [seen[num], i]
            seen[nums[i]]=i
        return []     
