class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pre = []
        maxx = 0
        for i in range(len(nums)):
            maxx = max(maxx, nums[i])
            pre.append(maxx)

        suff = []
        minn = float("inf")
        for l in range(len(nums)-1, -1, -1):
            minn = min(nums[l], minn)
            suff.append(minn)
        suff= suff[::-1]
       
        for j in range(len(nums)):
            if pre[j]-suff[j]<=k:
                return j
        return -1
        
        