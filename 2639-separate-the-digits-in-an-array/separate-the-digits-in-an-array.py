class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for ch in nums:
            x = list(map(int, list(str(ch))))
            ans.extend(x)
        return ans
        