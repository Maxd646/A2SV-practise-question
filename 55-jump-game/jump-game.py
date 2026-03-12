class Solution:
    def canJump(self, nums: List[int]) -> bool:
        long=0
        for i in range(len(nums)):
            if i>long:
                return False
            long = max(long, nums[i]+i)
        return True
        
        
        

            
            




            



        
        


        