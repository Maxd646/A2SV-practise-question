class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ans = total = left = 0
        n = len(nums)

        for i in range(n):

            if nums[i] == 1:

                total += 1
                ans = max(ans, total)
                continue

            if k > 0:

                total += 1
                k -= 1 
                ans = max(ans, total)
                continue
            
            while left < n and nums[left] == 1:

                left += 1
                total -= 1
                    
            k = 0
            left += 1
            ans = max(ans, total)
                    
        return ans




                


            
            
            
            
            
        