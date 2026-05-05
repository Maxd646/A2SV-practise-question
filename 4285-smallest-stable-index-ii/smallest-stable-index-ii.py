class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxx = 0
        suff = []
        minn = float("inf")
        for l in range(len(nums)-1, -1, -1):
            minn = min(nums[l], minn)
            suff.append(minn)
        suff= suff[::-1]
    
        for j in range(len(nums)):
            maxx = max(nums[j], maxx)
            if maxx-suff[j]<=k:
                return j
        return -1
        
        