class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans , pro = 0, 1
        left = 0

        for i in range(n):

            pro *= nums[i]
    
            while pro >= k and left < n:
                
                pro //= nums[left]
                left += 1

            ans += i - left +1

        return ans 


        