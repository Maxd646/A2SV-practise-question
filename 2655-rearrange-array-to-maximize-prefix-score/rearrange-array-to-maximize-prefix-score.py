class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n= len(nums)
        nums.sort(reverse =True)
        nums=list(accumulate(nums))
        print(nums)
    
        for i in range(n):
            if nums[i]<=0:
                return i
        return n



        

        