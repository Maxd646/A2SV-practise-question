class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        long = 0
        ans =0
        far =0
        for i in range(len(nums)):
            far = max(far, i+nums[i])
            if long >= len(nums) - 1:
                    break
            elif long==i:
                ans+=1
                long = far
        return ans

    


        