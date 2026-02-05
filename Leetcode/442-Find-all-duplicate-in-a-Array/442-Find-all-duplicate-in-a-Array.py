from collections import Counter
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        count=Counter(nums)
        result=[]
        for ch, num in count.items():
            if num>1:
                result.append(ch)
        return result
