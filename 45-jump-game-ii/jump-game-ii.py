class Solution:
    def jump(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 0

        ans = 0
        n  = len(nums)-1
        maxx = 0
        far = 0

        for i in range(n+1):

            far = max(nums[i]+i, far)

            if  maxx >= n:
                return ans 

            if maxx == i :
                ans+= 1
                maxx = far

        return ans 
            




        