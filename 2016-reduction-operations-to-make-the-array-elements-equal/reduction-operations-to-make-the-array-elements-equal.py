class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        seen = Counter(nums)
        seen = sorted(seen.items(), reverse=True)

        ans = 0
        total = 0
        minn = min(nums)

        for num, val in seen:

            if num != minn:
                
                total += val
                ans += total

        return ans
