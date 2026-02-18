# How Many Numbers Are Smaller Than the Current Number
# Platform: LeetCode
from collections import Counter
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        seen=Counter(nums)
        num = sorted(seen.items())
        small=0
        for num, val in num:
            seen[num]=small
            small+=val
        for i in range(len(nums)):
            nums[i]=seen[nums[i]]
        return nums
