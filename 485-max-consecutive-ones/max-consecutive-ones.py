class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        ans = total = 0

        for num in nums:

            if num == 1:

                total += 1
                continue

            ans = max(ans, total)
            total = 0
         
        return max(ans, total) 

            
