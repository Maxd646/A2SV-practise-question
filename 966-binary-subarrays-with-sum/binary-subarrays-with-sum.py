class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)
        
        def atmost(goal):
            
            if goal < 0:
                return 0

            summ  = 0
            ans = left = 0

            for i in range(n):

                summ += nums[i]

                while summ > goal and left < n:

                    summ -= nums[left]
                    left += 1

                ans += i - left +1

            return ans 
        
        return atmost(goal) - atmost(goal-1)

            
        