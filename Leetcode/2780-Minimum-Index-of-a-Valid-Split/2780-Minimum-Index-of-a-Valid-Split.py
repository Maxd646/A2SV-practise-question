# Minimum Index of a Valid Split
# Platform: LeetCode
from typing import List
from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        num, total= Counter(nums).most_common(1)[0]
        li=0
        for index, number in enumerate(nums):
            if number==num:
                li+=1
            liD=li*2>(index+1)
            ri=total-li
            riD=ri*2>len(nums)-(index+1)
            

            if liD and riD:
                return index
        return -1
