# Subarray Sum Equals K
# Platform: LeetCode
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n, summ, pre=0, 0, 0
        for num in nums:
            summ+=num
            if summ-k in pre:
                n+=pre[summ-k]
            pre[summ]=pre.get(summ, 0)+1
        return n
        
        
