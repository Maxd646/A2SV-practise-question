class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:

        seen = Counter(nums)

        seen1 = Counter(seen.values())
        
        for num in nums:

            if seen1[seen[num]] == 1:
                return num
        return -1
         



        
            



        