class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans =0
        for k in range(1, n+1):
            if n%k!=0:continue
            prevmax = -float("inf")
            ok = True
            for i in range(0, n, k):
                crmin = float("inf")
                crmax = - float("inf")
                monomax = 0
                for j in range(k):
                    crmin = min(crmin, nums[i+j])
                    crmax = max(crmax, nums[i+j])
                    if j<k-1 and nums[j+i]>nums[j+i+1]:
                        monomax+=1
                if nums[i+k-1]>nums[i]:
                    monomax+=1
                if crmin<prevmax or monomax>1:
                    ok = False
                    break
                prevmax = crmax
            if ok:
                ans+=k
        return ans


        
        
        
        