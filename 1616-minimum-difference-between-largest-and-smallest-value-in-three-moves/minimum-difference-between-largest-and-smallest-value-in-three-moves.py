class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums.sort()
        total=sum(nums)
        ans=float("inf")
        for i in range(4):
            ans= min(ans, nums[-4+i]-nums[i])
        return ans
        