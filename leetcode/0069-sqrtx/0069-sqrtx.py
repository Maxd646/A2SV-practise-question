class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left, right = 0, x//2
        ans =left
        while left<=right:
            mid = (left+right)//2
            if mid*mid ==x:
                return mid
            if mid*mid<x:
                ans = mid
                left = mid+1
            else:
                right = mid -1
        return ans




        