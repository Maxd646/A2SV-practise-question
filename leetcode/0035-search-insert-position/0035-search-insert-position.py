class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(left, right):
            if right<left:
                return left
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return search(left, mid-1)
            else:
                return search( mid+1, right)

        return search(0, len(nums)-1)
                

        