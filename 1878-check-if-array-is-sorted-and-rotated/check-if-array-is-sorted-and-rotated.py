class Solution:
    def check(self, nums: List[int]) -> bool:
        num = sorted(nums)
        for k in range(len(nums)):
            
            if nums ==(num[-k:]+num[:-k]):
                return True
        return False
        