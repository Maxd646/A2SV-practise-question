class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        summ = left = ans = 0

        for i in range(n):

            summ += nums[i]

            while summ*(i-left+1)>= k and left < n:

                summ -= nums[left]
                left += 1

            ans += i - left +1

        return ans

        