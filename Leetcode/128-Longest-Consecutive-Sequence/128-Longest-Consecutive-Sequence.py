# Longest Consecutive Sequence
# Platform: LeetCode

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums==[]:
            return 0
        num=list(set(nums))
        num.sort()
        maxx= 1
        count=1
        for i in range(len(num)-1):
            if num[i]+1==num[i+1]:
                count+=1
                maxx=max(count, maxx)
            else:
                count=1
        return maxx  
