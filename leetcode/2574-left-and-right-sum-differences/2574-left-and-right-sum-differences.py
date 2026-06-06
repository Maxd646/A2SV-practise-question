class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right = list(accumulate(nums))
        left = list(accumulate(nums[::-1]))
        right = [0]+right[:-1]
        left = [0] +left[:-1]
        left = left[::-1]
        print(right, left)
        ans = []
        for i in range(len(nums)):
            num = abs(right[i]- left[i])
            ans.append(num)
        return ans

        