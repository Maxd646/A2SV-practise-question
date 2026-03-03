# Continuous Subarray Sum
# Platform: LeetCode
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
            summ, pre= 0, 0
            for i in range(len(nums)):
                summ=(summ+nums[i])%k
                if summ in pre:
                    if i-pre[summ]>1:
                        return True
                else:
                    pre[summ]=i
            return False   
