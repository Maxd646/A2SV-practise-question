class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        left, right = 1, 1
        n = len(nums)
        ans = -float("inf")

        for i in range(n):

            if left == 0:
                left = 1

            if right == 0:
                right = 1

            left *= nums[i]
            right *= nums[n-i-1]
        
            ans = max(ans, max(left, right))
           
        return ans 
        
            
            
                
            
            
            
