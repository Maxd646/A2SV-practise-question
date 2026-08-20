class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        minn, maxx = min(nums), max(nums)
        minn, maxx = nums.index(minn),nums.index(maxx) 
        n = len(nums)
        x, y = min(minn, maxx), max(minn, maxx)
        return min(y+1, n-x, 1+x+n-y)


        
       
    
    
        


        