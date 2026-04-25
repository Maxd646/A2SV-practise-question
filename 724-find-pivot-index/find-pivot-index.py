class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total =sum(nums)
        left =0
        if sum(nums[1:])==0:
            return 0
        for i in range(1, len(nums)):
            left+=nums[i-1]
            if total== nums[i]+2*left:
                return i
        return -1
            
        
        