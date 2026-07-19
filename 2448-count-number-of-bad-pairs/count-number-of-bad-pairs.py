class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        seen = Counter()

        for pos in range(len(nums)):
            diff = pos - nums[pos]
            val = seen[diff]
            ans += pos - val
            seen[diff]= val+1
        return ans
        