# Maximum Sum Obtained of Any Permutation
# Platform: LeetCode
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count=[0]*len(nums)

        for l, r in requests:
            if r<len(nums)-1:
                count[r+1]-=1
            count[l]+=1

        count=list(accumulate(count))
        count.sort()
        nums.sort()
        ans=0

        for i in range(len(nums)):
            ans+=nums[i]*count[i]
        return ans%(10**9+7)

