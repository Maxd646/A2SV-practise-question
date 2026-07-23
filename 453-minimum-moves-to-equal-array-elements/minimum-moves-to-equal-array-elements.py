class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        minn= min(nums)
        for num in nums:
            ans+= (num-minn)
        return ans 