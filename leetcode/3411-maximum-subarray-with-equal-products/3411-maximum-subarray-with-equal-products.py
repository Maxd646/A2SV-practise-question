class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxx =0
        def GCD(nums):
            return reduce(gcd, nums)

        def LCM(nums):
            return reduce(lcm, nums)
            
        for i in range(n):
            for j in range(i, n):
                sub = nums[i:j+1]
                g= GCD(sub)
                l = LCM(sub)
                if prod(sub) == g*l:
                    maxx = max(maxx, j-i+1)
        return maxx
        

            
        