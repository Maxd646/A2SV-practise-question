#  Subarrays with K Different Integers
# Platform: LeetCode
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums, k):
            count= Counter()
            ans=0
            left=0
            for r in range(len(nums)):
                count[nums[r]]+=1
                while len(count)>k:
                    count[nums[left]]-=1
                    if count[nums[left]]==0:
                        del count[nums[left]]
                    left+=1
                ans+=r-left+1
            return ans
        return atmost(nums, k)- atmost(nums, k-1)

