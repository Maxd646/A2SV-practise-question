class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = sorted(Counter(nums).items())
        i =0
        prev =0
        for n, val in count:
            prev=i
            i +=val
            nums[prev:i] = [n]*val

        


        
        