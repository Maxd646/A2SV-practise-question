# Binary Subarrays With Sum
# Platform: LeetCode
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        summ,pre=0, 0
        n=0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ-goal in pre:
                n+=pre[summ-goal]
            pre[summ]=pre.get(summ, 0)+1
        return n
  
