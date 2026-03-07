class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        summ=sum(nums)
        ans=float("inf")
        n=len(nums)
        nums=nums+nums
        zo=nums[:summ].count(0)
        ans=zo
        for i in range(summ, n+summ):
            if nums[i]==0:
                zo+=1
            if nums[i-summ]==0:
                zo-=1
            ans=min(ans, zo)
        return ans
        