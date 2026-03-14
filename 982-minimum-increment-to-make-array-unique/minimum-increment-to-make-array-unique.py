class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        opt=0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1]<nums[i]:
                continue
            opt+=(-nums[i]+nums[i-1]+1)
            nums[i]=nums[i-1]+1
        return opt
            

        