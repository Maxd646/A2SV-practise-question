# Subarray Sums Divisible by K
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        summ, pre=0, 0
        n=0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ%k in pre:
                n+=pre[summ%k]
            pre[summ%k]=pre.get(summ%k, 0)+1
        return n

