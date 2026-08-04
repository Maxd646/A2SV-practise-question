class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        re=[]
        for i in range(min(nums), max(nums)+1):
            if i not in seen:
                re.append(i)
        return re
        