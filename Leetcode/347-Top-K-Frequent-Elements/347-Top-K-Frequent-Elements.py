# Top K Frequent Elements
# Platform: LeetCode
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count =Counter(nums)
        count=sorted(count.items(), key =lambda x:x[1], reverse=True)
        result=[]
        for ch, num in count:
            if len(result)<k:
                result.append(ch)
        return result
               
