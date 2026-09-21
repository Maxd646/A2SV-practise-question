class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:

        result = [0] * k
        dp = [0] * k

        for num in nums:

            ndp = [0] * k

            for r in range(k):
                if dp[r]:
                    new = (r * num) % k
                    ndp[new] += dp[r]

           
            ndp[num % k] += 1

         
            for r in range(k):

                result[r] += ndp[r]

            dp = ndp

        return result
        