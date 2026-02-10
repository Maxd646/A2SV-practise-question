# Find Original Array From Doubled Array
# Platform: LeetCode
from collections import Counter
from typing import List
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        result=[]
        count=Counter(changed)
        for num in changed:
            if count[num]==0:
                continue
            count[num]-=1
            double=num*2
            if count[double]<=0:
                return []
            count[double]-=1
            result.append(num)
        return result
