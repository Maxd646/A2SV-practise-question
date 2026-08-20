class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        minn, maxx = min(nums), max(nums)
        minn, maxx = nums.index(minn),nums.index(maxx) 
        n = len(nums)-1
        if minn == maxx:
            return maxx+1
        ans = float("inf")
        print(minn, maxx)
        if minn>maxx:
            ans = min(ans, minn+1)
            ans = min(ans, maxx+n-minn +2)
            ans = min(ans, n-maxx+1)
        if minn<maxx:
            ans = min(ans, maxx+1)
            ans = min(ans, minn+n-maxx+2)
            ans = min(ans, n-minn+1)
        return ans
    
    
        


        