class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ans = zero = left = 0
        n = len(nums)

        for i in range(n):

            if nums[i] == 0:
                zero += 1

            while zero > k and left < n:
                
                if nums[left] == 0:
                    zero -= 1
                left += 1

            ans = max(ans, i- left +1)

        return ans

            

                    
        return max(total, ans)




                


            
            
            
            
            
        