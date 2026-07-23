class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        avar = nums[len(nums)//2]
        ans = 0 
        for num in nums:
            ans += abs(avar-num)
        return ans
        