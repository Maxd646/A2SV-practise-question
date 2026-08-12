class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0

        left = 0
        seen = Counter()

        for i in range(len(nums)):

            seen[nums[i]] += 1

            if seen[nums[i]] >k:

                while seen[nums[i]] > k:

                    seen[nums[left]] -= 1
                    left += 1

            ans = max(ans, i-left+1)

        return ans

        