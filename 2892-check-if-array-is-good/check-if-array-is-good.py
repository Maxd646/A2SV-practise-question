class Solution:
    def isGood(self, nums: List[int]) -> bool:
        seen = set(nums)
        n = max(nums)
        if all( i in seen for i in range(1, n)):
            return nums.count(n) ==2 and len(list(set(nums))) == len(nums)-1
        return False
        