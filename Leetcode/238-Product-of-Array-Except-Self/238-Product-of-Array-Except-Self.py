# Product of Array Except Self
# Platform: LeetCode
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        re= [1]* len(nums)
        prif=sf=1
        for i in range(len(nums)):
            re[i]=prif
            prif*=nums[i]

        for i in range(len(nums)-1, -1, -1):
            re[i]*= sf
            sf*=nums[i]
        return re
        
