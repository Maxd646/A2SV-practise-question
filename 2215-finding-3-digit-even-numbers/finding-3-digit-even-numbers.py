class Solution:
    def findEvenNumbers(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if nums[k]%2==0 and j!=k and i!=k and i!=j and nums[i]!=0:
                        seen.add(100*nums[i]+10*nums[j]+nums[k])
        return sorted(list(seen))