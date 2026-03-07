class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum=[]
        rsum=[]
        summ=0
        for i in range(len(nums)):
            lsum.append(summ)
            summ+=nums[i]
        summ=0
        for i in range(len(nums)-1, -1, -1):
            rsum.append(summ)
            summ+=nums[i]

        rsum=rsum[::-1]

        ans=[]
        for i in range(len(nums)):
            ans.append(abs(rsum[i]-lsum[i]))
        return ans

        