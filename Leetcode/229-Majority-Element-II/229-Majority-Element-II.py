# Majority Element II
# Platform: LeetCode
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen= Counter(nums)
        result=[]
        for ch, num in seen.items():
            if num>len(nums)/3:
                result.append(ch)
        return result
