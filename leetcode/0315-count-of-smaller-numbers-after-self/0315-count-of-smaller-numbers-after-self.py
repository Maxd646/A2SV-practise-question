class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        ans = []
        res= []
        for i in range(len(nums)):
            l = bisect_left(res, nums[i])
            ans.append(l)
            insort(res, nums[i])
        return ans[::-1]

            
            


        