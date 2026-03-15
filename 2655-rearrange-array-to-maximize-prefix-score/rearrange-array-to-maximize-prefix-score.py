class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        j=0
        found=False
        for i in range(n):
            if nums[i]>0:
                j=i
                found=True
                break

        nums=list(accumulate(nums[j:]+nums[:j][::-1]))
    
        for i in range(n):
            if nums[i]<=0:
                return i
        return n



        

        