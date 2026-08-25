class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        seen = set(nums)
        i = k
        while True:
            if i not in seen:
                return i
            i += k
        