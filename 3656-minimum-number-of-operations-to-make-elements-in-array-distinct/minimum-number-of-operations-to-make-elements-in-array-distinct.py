class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        while len(nums)!=len(set(nums)):
            nums=nums[3:]
            ans+=1
        return ans



        
        