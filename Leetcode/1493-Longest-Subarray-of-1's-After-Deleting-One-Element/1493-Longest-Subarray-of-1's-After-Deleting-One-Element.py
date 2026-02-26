# Longest Subarray of 1's After Deleting One Element
# Platform: LeetCode
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        left=0
        summ=0
        for right in range(len(nums)):
            summ+=nums[right]
            while summ<right-left:
                summ-=nums[left]
                left+=1
            ans=max(ans, summ)
        if nums.count(0)==0:
            return ans-1
        return ans
