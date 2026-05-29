class Solution:
    def minElement(self, nums: List[int]) -> int:
        minn = float("inf")
        for i in range(len(nums)):
            minn = min(minn, sum(list(map(int, str(nums[i])))))
        return minn