class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        return sum(heapq.nlargest(2, nums))-min(nums)


        