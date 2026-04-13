class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        summ = sum(candies)
        if summ<k:
            return 0
        left, right = 1, summ//k
        ans =0
        while left<=right:
            mid =  (right +left)//2
            count =0
            for n in candies:
                if n>=mid:
                    count+=n//mid
                if count>=k:
                    break
            if count>=k:
                ans= mid
                left = mid + 1
            else:
                right = mid - 1 
        return ans

       

        