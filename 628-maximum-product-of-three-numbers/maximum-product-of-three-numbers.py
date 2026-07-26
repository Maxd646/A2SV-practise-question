class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        mm=nums[0]*nums[1]
        mmm=nums[-2]*nums[-3]
        if mm*nums[-1]>mmm*nums[-1]:
            return nums[-1]*mm
        else:
            return nums[-1]*mmm
        