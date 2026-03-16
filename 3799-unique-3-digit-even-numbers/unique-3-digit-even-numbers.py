
class Solution:
    def totalNumbers(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if nums[k]%2==0 and j!=k and i!=k and i!=j and nums[i]!=0:
                        seen.add(str(nums[i])+str(nums[j])+str(nums[k]))
        return len(seen)