# Largest Number
# Platform: LeetCode

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result=""
        nums=[str(num) for num in nums]
        num= "".join(sorted(nums, key= lambda x:x*10, reverse =True))
        if num[0]=="0":
            return "0"
        return num
