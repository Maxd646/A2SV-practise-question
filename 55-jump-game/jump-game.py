class Solution:
    def canJump(self, nums: list[int]) -> bool:


        n = len(nums)
        maxx = 0

        for i in range(n-1):
            if max(nums[i], maxx-i) <=0:
                return False
            
            maxx = max(nums[i]+i, maxx)

        return True


        


        