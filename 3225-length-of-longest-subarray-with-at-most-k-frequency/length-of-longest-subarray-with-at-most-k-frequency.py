class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0

        left = 0
        count = Counter()

        for i in range(len(nums)):

            count[nums[i]] += 1

            if count[nums[i]] >k:

                while count[nums[i]] > k:

                    count[nums[left]] -= 1
                    left += 1

            ans = max(ans, i-left+1)

        return ans

        