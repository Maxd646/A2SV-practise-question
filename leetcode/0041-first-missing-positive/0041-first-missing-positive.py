class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seeen = set(nums)
        for i in range(1, abs(max(nums))+1):
            if i not in seeen:
                return i
        return max(nums)+1
        
        
        