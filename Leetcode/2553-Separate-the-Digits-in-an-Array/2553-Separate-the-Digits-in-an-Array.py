# Separate the Digits in an Array
# Platform: LeetCode

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        for ch in nums:
            j=0
            m=str(ch)
            while j<len(m):
                result.append(int(m[j]))
                j+=1
        return result         
