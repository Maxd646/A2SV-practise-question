class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        t = sum(nums) - x

        if t < 0:
            return -1

        if t == 0:
            return len(nums)

        left = 0
        curr = 0
        longest = -1

        for right in range(len(nums)):
            curr += nums[right]

            while curr > t:
                curr -= nums[left]
                left += 1

            if curr == t:
                longest = max(longest, right - left + 1)

        return len(nums) - longest if longest != -1 else -1