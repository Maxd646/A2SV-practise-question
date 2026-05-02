class Solution:
    def minOperations(self, nums: list[int]) -> int:
        opr = 0
        for i in range(1, len(nums)):
            n =nums[i-1]-nums[i]
            if n>0:
                opr+=n
        return opr
