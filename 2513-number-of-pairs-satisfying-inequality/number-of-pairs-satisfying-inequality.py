from bisect import bisect_left
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        ans = 0

        for j in range(len(nums1)):
            val = nums1[j] - nums2[j]

            target = val + diff
            ans += bisect_left(arr, target + 1)

            insort(arr, val)
        
        return ans