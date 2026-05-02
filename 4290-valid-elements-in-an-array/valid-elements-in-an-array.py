class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums) ==1:
            return nums
        ans = [-1]*len(nums)
        maxx = -1
        a = 1
        for i in range(len(nums)):
            if nums[i]>maxx:
                maxx = nums[i]
                ans[i]= nums[i]

        maxx = -1
        for j in range(len(nums)-1, 0, -1):
            if nums[j]>maxx:
                ans[j] = nums[j]
                maxx = nums[j]

        return [num for num in ans if num!=-1]
            
    
        