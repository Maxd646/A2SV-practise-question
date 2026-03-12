class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        end = 0
        long = 0
        ans =0
        for i in range(len(nums)):
            long = max(long, nums[i]+i)
            if end == i: 
                ans+=1
                end=long
            if end >= len(nums) - 1:
                    break
        return ans

    


        