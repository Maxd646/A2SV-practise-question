#  H-Index
# Platform: LeetCode
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==1 and citations[0]!=0:
            return 1
        citations.sort(reverse=True)
        count=0
        for i in range(len(citations)):
            if count>=citations[i]:
                return count
            count+=1
        return count
